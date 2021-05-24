import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { Button, Typography } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  mobileButton: {
    background: "rgba(165, 147, 224, 1)",
    width: "70vw",
    borderRadius: "15px",
  },
  mobileButtonText: {
    color: "rgba(256, 256, 256, 1)",
    fontSize: "20px",
    fontWeight: "Bold",
  },
}));

export default function Buttons({ color, text, url }) {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Button className={classes.mobileButton}>
        <Typography className={classes.mobileButtonText}>{text}</Typography>
      </Button>
    </React.Fragment>
  );
}
