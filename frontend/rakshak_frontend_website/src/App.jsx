import "./App.css";

import { Route, Routes } from "react-router-dom";
import Authpage from "./pages/Authpage/index";
import Overview from "./pages/Overview/index";
import Mapview from "./pages/Mapview/index";
import Timeline from "./pages/Timeline/index";
import { StoreContext } from "./store/store";

function App() {
  return (
    <Routes>
      <Route path="/" Component={Overview} />
      <Route path="/signin" Component={Authpage} />
      <Route path="/timeline" Component={Timeline} />
      <Route path="/mapview" Component={Mapview} />
    </Routes>
  );
}

export default App;
