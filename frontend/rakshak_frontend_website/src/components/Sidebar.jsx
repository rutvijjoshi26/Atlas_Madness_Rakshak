import { Link } from "react-router-dom";
import Homeicon from "../Assets/Home.svg";
import Timelineicon from "../Assets/timeline_icon.png";

import Settingsicon from "../Assets/settings_icon.png";

const Sidebar = () => {
  return (
    <div className="flex flex-col min-h-[118vh] max-w-[15vw] bg-gray-100 drop-shadow-xl justify-between overflow-hidden p-2">
      <div>
        {/* Generate Report Button */}
        <div className="text-white text-lg text-ellipsis font-bold flex text-center flex-row justify-center py-8">
          <button className="bg-blue-800 rounded-md l px-5 py-2">
            <span className="font-extrabold text-2xl">+</span> Generate Report
          </button>
        </div>
        {/* Dashboard */}
        <Link to="/">
          <div className="flex flex-row justify-start gap-x-3 p-4 items-center">
            <div className="max-h-[20px] max-w-[20px] ml-4">
              <img className="object-cover" src={Homeicon} alt="Home icon" />
            </div>
            <div className="font-bold text-lg">Dashboard</div>
          </div>
        </Link>
        {/* Insights */}
        <div className="font-light text-lg text-gray-600 p-3">
          <span className="ml-5">INSIGHTS</span>
        </div>
        {/* Timeline */}
        <Link to="/timeline">
          <div className="flex flex-row justify-start gap-x-3 p-3 items-center">
            <div className="max-h-[20px] max-w-[20px] ml-4">
              <img
                src={Timelineicon}
                alt="Timeline icon"
                className="object-cover"
              ></img>
            </div>
            <div className="font-bold text-lg">Timeline</div>
          </div>
        </Link>
      </div>

      <div className="my-3">
        {/* Settings */}
        <div className="flex flex-row justify-start gap-x-3 p-3 items-center">
          <div className="max-h-[20px] max-w-[20px] ml-4">
            <img
              src={Settingsicon}
              alt="Map icon"
              className="object-cover"
            ></img>
          </div>
          <div className="font-bold text-lg">Settings</div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
