(function () {
  // Initialize variables for debouncing and limiting data
  let timeoutId = null;
  const debounceDelay = 5; // milliseconds
  const maxDataSize = 1000000; // bytes
  let lastUrl = window.location.href;
  let lastData = null;

  // Define function for sending data to background script
  const sendDataToBackground = () => {
    const url = window.location.href;
    if (url !== lastUrl) {
      return;
    }
    // Extract page content
    const pageText = document.body.innerText;
    const imgElements = Array.from(document.getElementsByTagName("img"));
    const imgSrcs = imgElements
      .filter((img) => img.width >= 100 && img.height >= 100)
      .map((img) => img.src);
    const videoElements = Array.from(document.getElementsByTagName("video"));
    const videoSrcs = videoElements.map((video) => video.src);
    const audioSrcs = Array.from(document.getElementsByTagName("audio")).map(
      (audio) => audio.src
    );
    // Create data object to be sent to background script
    const data = {
      url,
      pageText,
      imgSrcs,
      videoSrcs,
      audioSrcs,
    };

    // Limit data size before sending
    const dataSize = new Blob([JSON.stringify(data)]).size;
    if (
      dataSize <= maxDataSize &&
      JSON.stringify(data) !== JSON.stringify(lastData)
    ) {
      // Send data to background script
      chrome.runtime.sendMessage({ type: "pageContent", data });
      lastData = data;
    } else {
      console.log(
        "Data size limit exceeded or same data as previous interval. Data not sent."
      );
    }
  };

  // Define function for handling load events on images, videos, and audios
  const handleLoadEvent = () => {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    timeoutId = setTimeout(() => {
      sendDataToBackground();
    }, debounceDelay);
  };

  // Listen for load event on the parent element of all images, videos, and audios
  document.body.addEventListener(
    "load",
    (event) => {
      const element = event.target;
      if (
        element.tagName === "img" ||
        element.tagName === "video" ||
        element.tagName === "audio"
      ) {
        handleLoadEvent();
      }
    },
    false
  );

  // Function to handle the response from the background script
  const handleResponse = (response) => {
    if (response.data["result"] === "NSFW") {
      var overlay = document.createElement("div");
      overlay.id = "white-page-overlay";

      // Style the overlay to cover the entire screen
      overlay.style.position = "fixed";
      overlay.style.top = "0";
      overlay.style.left = "0";
      overlay.style.width = "100%";
      overlay.style.height = "100%";
      overlay.style.backgroundColor = "white";
      overlay.style.zIndex = "9999";

      // Create a text element to display the message
      var messageText = document.createElement("p");
      messageText.textContent = "The content you are viewing is Obscene";
      messageText.style.position = "absolute";
      messageText.style.top = "50%";
      messageText.style.left = "50%";
      messageText.style.transform = "translate(-50%, -50%)";
      messageText.style.fontSize = "24px";

      // Append the text element to the overlay
      overlay.appendChild(messageText);

      // Append the overlay to the document body
      document.body.appendChild(overlay);
    }
  };

  // Send initial page content
  sendDataToBackground();

  // Rescan the page after every 20 seconds
  setInterval(() => {
    sendDataToBackground();
  }, 30000); // Changed interval from 25 seconds to 20 seconds

  // Listen for messages from the background script
  chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === "serverResponse") {
      handleResponse(message);
    }
  });
})();
