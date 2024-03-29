import React, { Fragment, useState } from "react";
import countdown from "./countdown.gif";

const Countdown = props => {
  const [visibility, setVisibility] = useState(true);

  setTimeout(() => {
    setVisibility(false);
  }, 2700);
  let style = { width: "70%", margin: "auto", display: "block" };
  if (!visibility) style.display = "none";

  return (
    <Fragment>
      <img src={countdown} alt="Loading..." style={style} />
    </Fragment>
  );
};

export default Countdown;
