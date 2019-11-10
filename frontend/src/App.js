import React, { useState } from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "./components/pages/Home";
import Guess from "./components/pages/Guess";
import NotFound from "./components/pages/NotFound";

const App = () => {
  const [genre, setGenre] = useState("");

  return (
    <Router>
      <Switch>
        <Route
          exact
          path="/"
          render={props => <Home {...props} setGenre={setGenre} />}
        />
        <Route
          exact
          path="/Guess"
          render={props => <Guess {...props} genre={genre} />}
        />
        <Route component={NotFound} />
      </Switch>
    </Router>
  );
};

export default App;
