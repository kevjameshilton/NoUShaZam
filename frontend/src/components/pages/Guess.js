import React, { Fragment } from "react";
import Countdown from "./../layout/Countdown";

const Guess = props => {
  return (
    <Fragment>
      <h1 className="text-center text-primary">{props.genre}</h1>
      <Countdown />
    </Fragment>
  );
};

export default Guess;
