import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import AppNavBar from "./components/AppNavBar";
import { authenticate } from "./store/session";
import Landing from './components/Landing';
import Footer from './components/Footer'
// import Navigation from "./components/Navigation";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      {/* <Navigation isLoaded={isLoaded} /> */}
      <AppNavBar />
      {/* {isLoaded && ( */}
          <Switch>
            <Route exact path="/" >
              <Landing />
            </Route>
            <Route exact path="/login" >
              <LoginFormPage />
            </Route>
            <Route exact path="/signup" >
              <SignupFormPage />
            </Route>
          </Switch>
      {/* )} */}
      <Footer />
    </>
  );
}

export default App;
