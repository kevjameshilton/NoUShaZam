import React, { Fragment } from "react";

const Dashboard = props => {
  return (
    <Fragment>
      <button
        genre="Pop"
        className="btn my-2 btn-dark"
        onClick={() => props.setGenre("Pop")}
      >
        Pop
      </button>
      <button
        genre="Hip Hop"
        className="btn my-2 btn-dark"
        onClick={() => props.setGenre("Hip Hop")}
      >
        Hip Hop
      </button>
      <button
        genre="Rock"
        className="btn my-2 btn-dark"
        onClick={() => props.setGenre("Rock")}
      >
        Rock
      </button>
      <button
        genre="Jazz"
        className="btn my-2 btn-dark"
        onClick={() => props.setGenre("Jazz")}
      >
        Jazz
      </button>
      <button
        genre="Anime"
        className="btn my-2 btn-dark"
        onClick={() => props.setGenre("Anime")}
      >
        Anime
      </button>
      <button
        genre="80s"
        className="btn my-2 btn-dark"
        onClick={() => props.setGenre("80s")}
      >
        80s
      </button>
      <button
        genre="90s"
        className="btn my-2 btn-dark"
        onClick={() => props.setGenre("90s")}
      >
        90s
      </button>
      <button
        genre="Classical"
        className="btn my-2 btn-dark"
        onClick={() => props.setGenre("Classical")}
      >
        Classical
      </button>
    </Fragment>
  );
};

export default Dashboard;
