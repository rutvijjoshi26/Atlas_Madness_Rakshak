import React, { useContext, useEffect } from "react";
import Sidebar from "../../components/Sidebar";
import Header from "../../components/Header";
import Body from "./Body";

const Timeline = () => {

  return (
    <div className="flex">
      <div className="w-auto bg-gray-200">
        <Sidebar />
      </div>

      <div className="flex flex-col w-[85%] ">
        <Header />
        <div>
          <Body />
        </div>
      </div>
    </div>
  );
};

export default Timeline;
