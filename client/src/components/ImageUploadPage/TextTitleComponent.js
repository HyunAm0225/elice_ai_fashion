import React from "react";
import { Box, Typography } from "@material-ui/core";
import { useStyles } from "../../styles/ImageUploadPageStyles";


export default function TextTitleComponent({title, subtitle}) {
    const classes = useStyles();

    return (
      <Box>
        <Box className={classes.mobileTitleBox}>
          <Typography className={classes.mobileTitleText}>{title}</Typography>
        </Box>
        <Box className={classes.mobileTitleBox}>
          <Typography className={classes.mobileSubtitleText}>
            {subtitle}
          </Typography>
        </Box>
      </Box>
    );
  }