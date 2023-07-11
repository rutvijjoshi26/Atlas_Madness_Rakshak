import { ResponsiveCalendar } from "@nivo/calendar";

const MyResponsiveCalendar = ({ mydata }) => {

  const currentDate = new Date();
  const formattedCurrentDate = currentDate.toISOString().slice(0, 10);

  // First day of the current year
  const firstDayOfYear = new Date(currentDate.getFullYear(), 0, 1);
  const formattedFirstDayOfYear = firstDayOfYear.toISOString().slice(0, 10);

  // Adjusting first day of the year to current year
  const currentYearFirstDay = `${currentDate.getFullYear()}-01-01`;
  return (
    <ResponsiveCalendar
      data={mydata.length !== 0 ? mydata[0]["data"] : mydata}
      from={currentYearFirstDay}
      to={formattedCurrentDate}
      emptyColor="#eeeeee"
      colors={["#61cdbb", "#97e3d5", "#e8c1a0", "#f47560"]}
      margin={{ top: 20, bottom: 10 }}
      yearSpacing={40}
      monthBorderColor="#ffffff"
      dayBorderWidth={2}
      dayBorderColor="#ffffff"
      legends={[
        {
          anchor: "bottom-right",
          direction: "row",
          translateY: 36,
          itemCount: 4,
          itemWidth: 50,
          itemHeight: 40,
          itemsSpacing: 20,
          itemDirection: "right-to-left",
        },
      ]}
    />
  );
};

export default MyResponsiveCalendar;
