import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import Button from '@mui/material/Button';

import { Redirect } from "react-router-dom";
import './LoginForm.css';
import logImage from "./log.png"


const LoginFormPage = () => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    window.alert("Form Submitted!")
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  return (
    <div className="login-container">
      <img
        src={ logImage }
        className="login-image"
        alt="its a log"
      />
      <div className="login-box">
        <h1 className="login-title"> Log On </h1>
        <form 
          onSubmit={handleSubmit}
          className="login-form"  
        >
          <ul>
            {errors.map((error, idx) => (
              <li key={idx}>{error}</li>
              ))}
          </ul>
          <label className="login-form-label" name="email">
            Email:
          </label >
          <input
              type="text"
              label="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="login-input"
              placeholder="email"
          />
          <label className="login-form-label" name="password">
            Password:
          </label>
          <input
              type="password"
              value={password}
              label="password"
              onChange={(e) => setPassword(e.target.value)}
              required
              className="login-input"
              placeholder="••••••••"
           />
          <Button 
            variant="outlined"
            size="large"
            type="submit"
            sx={{
                color: "whitesmoke",
                border: 3,
                borderColor: "whitesmoke",
                borderRadius: 2,
                margin: 2,
                bgcolor: "darkgreen",
                '&:hover': {
                    bgcolor: "orange",
                }
            }}
        >
          Log On
        </ Button>
        </form>
      </div>
      <img 
        src={ logImage }
        className="login-image"
        alt="its a log"
      />
      
    </div>
  );
}

export default LoginFormPage;
