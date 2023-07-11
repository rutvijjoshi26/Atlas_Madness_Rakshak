import { useEffect, useState } from "react";
import { get_timeline_numbers } from "../../hooks/Timeline_numbers";
import { get_timeline_bump_chart_data } from "../../hooks/Timeline_bump_chart";
import { get_timeline_calender } from "../../hooks/Timeline_Calender";
import { getFilteredData } from "./Filtered_data";
import Toplevel_toggle from "./Toplevel_toggle";
import MyResponsiveBump from "../../Charts/ResponsiveBumpChart";
import MyResponsiveCalendar from "../../Charts/ResponsiveCalender";
import Loading from "../../components/Loading";
import Card from "../../components/Card";

const Body = () => {
  const toggle_buttons = ["image", "text", "video", "audio"];
  const [top_level_toggle, Set_top_level_toggle] = useState("image");
  const [numbers_data, Setnumbers_data] = useState({});
  const [bum_chart_data, Setbump_chart_data] = useState([]);
  const [calender_data, Setcalender_data] = useState([]);
  const [loading, Setloading] = useState(false);

  const choose_toggle = (toggle_value) => {
    Set_top_level_toggle(toggle_value);
  };

  useEffect(() => {
    const getData = async () => {
      let counter = 0; // Counter variable to keep track of completed requests

      // Function to increment the counter and check if all requests are completed
      const checkAllRequestsCompleted = () => {
        counter++;
        if (counter === 3) {
          // All requests are completed, set loading to false
          Setloading(false);
        }
      };

      Setloading(true);

      try {
        const number_data = await get_timeline_numbers();
        Setnumbers_data(number_data);
        checkAllRequestsCompleted(); // Increment counter for numbers_data request
      } catch (error) {
        console.error(error.message);
        checkAllRequestsCompleted(); // Increment counter even if there's an error
      }

      try {
        const bump_data = await get_timeline_bump_chart_data();
        Setbump_chart_data(bump_data);
        checkAllRequestsCompleted(); // Increment counter for bump_chart_data request
      } catch (error) {
        console.error(error.message);
        checkAllRequestsCompleted(); // Increment counter even if there's an error
      }

      try {
        const calender_data_main = await get_timeline_calender();
        Setcalender_data(calender_data_main);
        checkAllRequestsCompleted(); // Increment counter for calender_data request
      } catch (error) {
        console.error(error.message);
        checkAllRequestsCompleted(); // Increment counter even if there's an error
      }
    };

    getData();
  }, []);

  const filtered_data = getFilteredData(numbers_data, top_level_toggle);
  const filtered_calender_data = calender_data.filter(
    (item) => item.file_type === top_level_toggle
  );
  const filtered_bump_chart_data = bum_chart_data.filter(
    (item) => item.id === top_level_toggle
  );
  return (
    <>
      {loading === false ? (
        <div className="flex flex-col rounded-lg bg-gray-100 min-w-full max-h-[100vh] overflow-hidden  py-2 px-2 justify-evenly ">
          <div className="flex flex-row justify-evenly items-center">
            {toggle_buttons.map((value, key) => (
              <Toplevel_toggle
                key={key}
                value={value}
                change_toggle={choose_toggle}
                current_toggle={top_level_toggle}
              />
            ))}
          </div>
          <div className="flex flex-row justify-evenly items-center">
            {Object?.entries(filtered_data).map(([key, value]) => (
              <Card key={key} title={key} value={value} />
            ))}
          </div>
          <div className="flex flex-col text-xl font-bold text-black">
            <div>Distribution of NSFW/SFW</div>
            <div className="inset-0 h-[30vh] w-full object-cover object-center transition duration-200 group-hover:scale-110 rounded-lg bg-white p-2 m-1">
              <MyResponsiveBump mydata={filtered_bump_chart_data} />
            </div>
          </div>
          <div className="flex flex-col text-xl font-bold text-black">
            <div>Daily NSFW Counts</div>
            <div className="inset-0 h-[30vh] w-full object-cover object-center transition duration-200 group-hover:scale-110 rounded-lg bg-white p-2 m-1">
              <MyResponsiveCalendar mydata={filtered_calender_data} />
            </div>
          </div>
        </div>
      ) : (
        <Loading />
      )}
    </>
  );
};

export default Body;
