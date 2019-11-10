import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import Dashboard from "../layout/Dashboard";

const Home = props => {
  return (
    <Fragment>
      <h1 className="text-center text-primary">NoUShaZam</h1>
      <Link to="/Guess" className="grid-2" genre="Pop">
        <Dashboard setGenre={props.setGenre} />
      </Link>
    </Fragment>
  );
};

export default Home;
