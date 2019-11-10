import React, { Fragment } from "react";

const Home = () => {
  return (
    <Fragment>
      <h1 className="text-center text-primary">NoUShaZam</h1>
      <div className="grid-2">
        <button className="btn my-2 btn-dark">Hip Hop</button>
        <button className="btn my-2 btn-dark">Pop</button>
        <button className="btn my-2 btn-dark">Rock</button>
        <button className="btn my-2 btn-dark">Jazz</button>
        <button className="btn my-2 btn-dark">Anime</button>
        <button className="btn my-2 btn-dark">80s</button>
        <button className="btn my-2 btn-dark">90s</button>
        <button className="btn my-2 btn-dark">Classical</button>
      </div>
    </Fragment>
  );
};

export default Home;
