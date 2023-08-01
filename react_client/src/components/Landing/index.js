import * as React from 'react';
import Paper from '@mui/material/Paper';
// Style import
import "./Landing.css"
import campPic from "./campsite.png"

const Landing = () => {
  return (
    <Paper 
        elevation={3}
        sx={{
            width: "auto",
            heigh: "auto",
            bgcolor: "darkgreen",
            color: "whitesmoke",
            fontFamily: "Roboto",
            display: "flex",
            flexDirection: "row",
            justifyContent: "center",
            alignItems: "center",
            border: 2,
            borderColor: "whitesmoke",
            borderRadius: "10px",
            padding: "10px",
        }} 
    >
        <div  className="landing-text-container">
            <div className="landing-text-sub-container">
                <p className="landing-title">BSA Troop 27</p>
                <p className="landing-sub-title">Glen Rock, NJ</p>
            </div>
            <div>
                <p className="landing-quote">"Scouting is all about learning stuff, and burning stuff..."</p>
                <p className="landing-author"> - A. Mazuti </p>    
            </div>
        </div>
        <img 
            src={ campPic }
            className="landing-graphic"
            alt="camping logo"
        />
    </ Paper>
  );
}

export default Landing;