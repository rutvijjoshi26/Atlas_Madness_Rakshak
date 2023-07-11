import { useEffect, useState } from "react";
import MyResponsiveAreaBump from "./../../Charts/ResponsiveAreaBump";
import MyResponsiveStream from "./../../Charts/ResponsiveStream";
import { get_overview_numbers } from "../../hooks/Overview_numbers";
import { get_overview_alerts } from "../../hooks/Overview_alearts";
import { get_overview_trending } from "../../hooks/Overview_trending";
import Loading from "../../components/Loading";
import Card from "../../components/Card";

const Body = () => {
  const [overview_numbers, Setoverview_numbers] = useState({});
  const [loading, Setloading] = useState(false);
  const [overview_trending, Setoverview_trending] = useState([]);
  const [overview_alerts, Setoverview_alerts] = useState([]);

  useEffect(() => {
    const getData = async () => {
      let counter = 0;
      const checkAllRequestsCompleted = () => {
        counter++;
        if (counter === 3) {
          // All requests are completed, set loading to false
          Setloading(false);
        }
      };
      Setloading(true);
      try {
        const overview_number_data = await get_overview_numbers();
        Setoverview_numbers(overview_number_data);
        checkAllRequestsCompleted();
      } catch (error) {
        checkAllRequestsCompleted();
        alert(error.message);
      }
      try {
        const overview_trending_data = await get_overview_trending();
        Setoverview_trending(overview_trending_data);
        checkAllRequestsCompleted();
      } catch (error) {
        checkAllRequestsCompleted();
        alert(error.message);
      }
      try {
        const overview_alerts_data = await get_overview_alerts();
        Setoverview_alerts(overview_alerts_data);
        checkAllRequestsCompleted();
      } catch (error) {
        checkAllRequestsCompleted();
        alert(error.message);
      }
    };
    getData();
  }, []);

  const format_date_function = (date_inp) => {
    const date = new Date(date_inp);
    const formatted_date = date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    });
    return formatted_date;
  };

  return (
    <>
      {loading === false ? (
        <>
          <div className="flex flex-wrap">
            {Object?.keys(overview_numbers).map((key) => (
              <Card key={key} title={key} value={overview_numbers[key]} />
            ))}
          </div>

          {/* This is the graph section */}

          <div className="bg-white py-6 sm:py-8 lg:py-12">
            <div className="mx-auto max-w-screen-2xl px-4 md:px-8 ">
              <div className="grid gap-6 grid-cols-3">
                <div className="group relative col-span-2 flex h-[30vh] w-100 items-end overflow-hidden rounded-lg bg-gray-100 p-3 shadow-lg">
                  <div
                    alt="An area bump Chart "
                    className=" inset-0 h-full w-full object-cover object-center transition duration-200 group-hover:scale-110"
                  >
                    <MyResponsiveAreaBump />
                  </div>

                  <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-gray-800 via-transparent to-transparent opacity-50"></div>
                </div>

                <div className="group relative flex h-[30vh] w-100 items-end overflow-hidden rounded-lg bg-gray-100 p-4 shadow-lg">


                  <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-gray-800 via-transparent to-transparent opacity-50"></div>

                  <div className="group relative flex h-[30vh] w-full items-end overflow-hidden rounded-lg bg-gray-100 p-4 shadow-lg">
                    {/* Inserted divs start */}
                    <div className="flex flex-col w-full h-full bg-gray-100">
                      <h2 className="text-lg font-semibold mb-2 mt-2">
                        Alerts
                      </h2>
                      {overview_alerts.map((item, index) => (
                        <div
                          key={index}
                          className="w-full bg-white p-4 mb-2 rounded shadow flex flex-row items-center justify-between"
                        >
                          <div>
                            {format_date_function(item["date_of_acquisition"])}
                          </div>
                          <div>{item["counter"]}</div>
                        </div>
                      ))}
                      <div className="flex-grow"></div>{" "}
                      {/* Added to fill remaining space */}
                    </div>
                    {/* Inserted divs end */}
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-white py-6 sm:py-8 lg:py-12">
            <div className="mx-auto max-w-screen-2xl px-4 md:px-8 ">
              <div className="grid gap-6 grid-cols-3">
                <div className="group relative col-span-2 flex h-[35vh] w-100 items-end overflow-hidden rounded-lg bg-gray-100 p-2 shadow-lg">
                  <div
                    loading="lazy"
                    alt="An area bump Chart "
                    className=" inset-0 h-full w-full object-cover object-center transition duration-200 group-hover:scale-110"
                  >
                    <MyResponsiveStream />
                  </div>

                  <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-gray-800 via-transparent to-transparent opacity-50"></div>
                </div>

                <div className="group relative flex h-[35vh] w-100 items-end overflow-hidden rounded-lg bg-gray-100 p-4 shadow-lg">

                  <div className="pointer-events-none absolute inset-0  opacity-50"></div>

                  <div className="group relative flex h-[35vh] w-full items-end overflow-hidden rounded-lg bg-gray-100 p-4 shadow-lg">
                    {/* Inserted divs start */}
                    <div className="flex flex-col w-full h-full bg-gray-100">
                      <h2 className="text-lg font-semibold mb-2 mt-2">
                        Notifications
                      </h2>
                      {overview_trending.map((item, index) => (
                        <div
                          key={index}
                          className="w-full bg-white p-4 mb-2 rounded shadow flex flex-row items-center justify-between"
                        >
                          <div>{item["result"]}</div>
                          <div>{item["counter"]}</div>
                        </div>
                      ))}
                      <div className="flex-grow"></div>{" "}
                      {/* Added to fill remaining space */}
                    </div>
                    {/* Inserted divs end */}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </>
      ) : (
        <Loading />
      )}
    </>
  );
};

export default Body;