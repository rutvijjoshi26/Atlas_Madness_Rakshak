const Card = ({ title, value }) => {
  return (
    <div className="w-1/4 p-4">
      <div className="bg-white rounded-lg shadow-lg p-6 flex flex-col">
        <div className="font-extrabold text-black text-xl">{value}</div>
        <div className="font-semibold text-base text-black">{title}</div>
      </div>
    </div>
  );
};

export default Card;
