import React, { Fragment, useState } from "react";
import countdown from "./countdown.gif";
import axios from "axios";

const Countdown = props => {
  const [visibility, setVisibility] = useState(true);

  setTimeout(() => {
    setVisibility(false);
    axios
      .get(`/song/${props.genre}`)
      .then(res => {
        console.log(res.song);
      })
      .catch(err => {
        console.log("There was an error in requesting the song");
      });
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
