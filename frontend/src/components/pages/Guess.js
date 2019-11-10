import React, { Fragment, useState } from "react";

const Guess = props => {
  const [genre, setGenre] = useState("");

  return (
    <Fragment>
      <h1 className="text-center text-primary">{props.genre}</h1>
    </Fragment>
  );
};

export default Guess;
