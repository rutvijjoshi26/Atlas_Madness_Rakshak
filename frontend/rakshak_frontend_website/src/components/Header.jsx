import React, { useState } from "react";
import Websitelogo from "../Assets/Rakshak_icon.png";
// import avatar from "../Assets/avatar.png";
import bell_icon from "../Assets/bell_icon.png";

const Header = () => {
  const [serachitem, Setsearchitem] = useState("");
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(serachitem);
  };
  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSubmit(e);
    }
  };
  return (
    <div className="flex flex-row items-center justify-between bg-gray-100 min-h-[5vh] min-w-screen drop-shadow-xl">
      {/* Website logo */}
      <div className="font-extrabold flex flex-row gap-3 p-3 items-center mx-3">
        <div className="max-h-[50px] max-w-[50px]">
          <img src={Websitelogo} className="object-cover" alt="Website logo" />
        </div>
        <div>
          <span className="text-2xl">RAKSHAK</span>
        </div>
      </div>
      {/* Search Bar */}
      <div className="min-w-[40%]">
        <input
          value={serachitem}
          onChange={(e) => Setsearchitem(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Search..."
          className="bg-gray-100 drop-shadow-xl rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 flex-grow px-6 py-3 w-full "
        />
      </div>
      <div className="flex flex-row gap-x-7 items-center p-4">
        <div className="cursor-pointer max-h-[40px] max-w-[40px]">
          <img
            src={bell_icon}
            alt="Notification Icon"
            className="object-cover"
          />
        </div>
        {/* <div className="   max-h-[50px] max-w-[60px] drop-shadow-lg">
          <img src={avatar} alt="User avatar" className="object-cover" />
        </div> */}
      </div>
    </div>
  );
};

export default Header;
