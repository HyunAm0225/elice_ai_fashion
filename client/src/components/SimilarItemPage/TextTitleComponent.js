import React from "react";
import { Box, Typography } from "@material-ui/core";
import { useStyles } from "../../styles/ImageUploadPageStyles";


export default function TextTitleComponent({title, number}) {
    const classes = useStyles();

    return (
      <Box>
        <Box className={classes.mobileTitleBox}>
          <Typography className={classes.mobileTitleText}>{title} {number}</Typography>
        </Box>
      </Box>
    );
  }