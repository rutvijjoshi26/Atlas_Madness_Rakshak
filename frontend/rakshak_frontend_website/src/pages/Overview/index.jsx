import Header from "../../components/Header";
import Sidebar from "../../components/Sidebar";
import Body from "./Body";

const Overview = () => {
  return (
    <div className="flex">
      <div className="w-auto bg-gray-200">
        <Sidebar />
      </div>

      <div className="flex flex-col w-[85%]">
        <Header />
        <div>
          <Body />
        </div>
      </div>
    </div>
  );
};

export default Overview;
