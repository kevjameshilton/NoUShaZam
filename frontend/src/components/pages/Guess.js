import React, { Fragment } from "react";
import Countdown from "./../layout/Countdown";
import { Link } from "react-router-dom";

const Guess = props => {
  return (
    <Fragment>
      <Link to="/">
        <button className="btn btn-dark">Back</button>
      </Link>
      <h1 className="text-center text-primary">{props.genre}</h1>
      <Countdown genre={props.genre} />
    </Fragment>
  );
};

export default Guess;
