import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { Button, Typography } from "@material-ui/core";

import { useHistory } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  mobileButton: {
    textDecoration: "none",
    background: "var(--color-main-a)",
    width: "70vw",
    borderRadius: "15px",
    color: "var(--color-bg-light)",
    underline: "none",

    "&.MuiButton-root:hover": {
      background: "var(--color-main-a)",
      color: "var(--color-bg-light)",
    },
  },
  mobileButtonText: {
    fontSize: "20px",
    fontWeight: "Bold",
    underline: "none",
  },
}));

export default function Buttons({ color, text, url }) {
  const classes = useStyles();
  const history = useHistory();

  function handleOnClick() {
    history.push(url);
  }

  return (
    <Button className={classes.mobileButton} onClick={handleOnClick}>
      <Typography className={classes.mobileButtonText}>{text}</Typography>
    </Button>
  );
}
