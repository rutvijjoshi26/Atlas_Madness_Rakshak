import React from "react";

const Toplevel_toggle = ({ value, change_toggle, current_toggle }) => {
  return (
    <div
      className={`min-w-[20%] items-center flex flex-row text-xl font-bold text-black bg-white rounded-lg justify-center p-5 cursor-pointer`}
      style={{
        outline: current_toggle === value ? "2px solid blue" : "none",
      }}
      onClick={() => change_toggle(value)}
    >
      {value}
    </div>
  );
};

export default Toplevel_toggle;
