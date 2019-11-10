import React, { Fragment, useEffect } from "react";
import Countdown from "./../layout/Countdown";
import { Link } from "react-router-dom";
import axios from "axios";

const Guess = props => {
  const genre = props.genre.toLowerCase();
  useEffect(() => {
    setTimeout(() => {
      axios
        .get(`/song/${genre}`)
        .then(res => {
          console.log(res.data);
        })
        .catch(err => {
          console.log("There was an error in requesting the song");
        });
    }, 2700);
  }, [genre]);

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
