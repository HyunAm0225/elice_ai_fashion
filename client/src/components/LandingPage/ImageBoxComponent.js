import React from "react";
import { Grid } from "@material-ui/core";
import { useStyles } from "styles/ImageUploadPageStyles";

export default function ImageBoxComponent({ src, inputtype, user_id }) {
  const classes = useStyles();

  return (
    <Grid
      className={classes.mobileClosetImageGrid}
      inputtype={inputtype}
      onClick={() => {}}
      item
      xs={4}
    >
      <Grid container className={classes.mobileEmptyImageBox}>
        <img className={classes.mobileImage} src={src} alt="none" />
      </Grid>
    </Grid>
  );
}
