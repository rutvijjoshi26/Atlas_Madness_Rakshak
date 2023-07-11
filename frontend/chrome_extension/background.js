// Listen for messages from the content script
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  if (message.type === "pageContent") {
    var url = message.data.url;
    var pageText = message.data.pageText;
    var imgSrcs = message.data.imgSrcs;
    var videoSrcs = message.data.videoSrcs;

    chrome.storage.local.get({ urls: {} }, function (result) {
      var urls = new Set(Object.keys(result.urls));
      if (urls.has(url)) {
        
        sendResponse({ status: "Cache hit" });
        return;
      }
      var limit = 5;
      var filteredImgSrc = filterUrls(imgSrcs, limit);
      var filteredVideoSrc = filterUrls(videoSrcs, limit);

      sendRequest(filteredImgSrc, "image", sender.tab.id);

      sendRequest(filteredVideoSrc, "video", sender.tab.id);
      sendTextRequest(pageText, sender.tab.id);

      urls.add(url);
      const sortedUrls = mergeSort(Array.from(urls));

      sendResponse({ status: "Cache updated" });
    });

    // Preserve the connection for async response
    return true;
  }
});

// Function to send a message to the specific content script
function sendMessageToContentScript(tabId, response) {
  chrome.tabs.sendMessage(tabId, { type: "serverResponse", data: response });
}

// Function to send requests for URLs of a specific type
function sendRequest(urls, type, tabId) {
  console.log(urls);
  if (urls.length > 0) {
    fetch(`https://${type}-dot-optimum-bonbon-392016.uc.r.appspot.com/api/nsfw/${type}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ urls: urls }),
    })
      .then(function (response) {
        if (!response.ok) {
          throw new Error("Request failed with status: " + response.status);
        }
        return response.json();
      })
      .then(function (data) {
        console.log(data)
        sendMessageToContentScript(tabId, data); // Send the response to the specific content script
      })
      .catch(function (error) {
        console.error("Error:", error);
      });
  }
}

// Function to send a text request
function sendTextRequest(text, tabId) {
  fetch("https://text-dot-optimum-bonbon-392016.uc.r.appspot.com/api/nsfw/text", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: text }),
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      sendMessageToContentScript(tabId, data);
    })
    .catch(function (error) {
      console.error("Error:", error);
    });
}

// Function to sort URLs using merge sort algorithm
function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);

  return merge(mergeSort(left), mergeSort(right));
}

// Function to merge two sorted arrays
function merge(left, right) {
  const result = [];

  while (left.length && right.length) {
    if (left[0] <= right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }

  return [...result, ...left, ...right];
}

// Function to filter URLs and limit the number of results
function filterUrls(urls, limit) {
  return urls
    .filter(function (url) {
      return url.trim() != "";
    })
    .slice(0, limit);
}
