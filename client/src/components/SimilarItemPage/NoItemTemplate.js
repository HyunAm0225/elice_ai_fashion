import React from "react";
import { Box, Typography } from "@material-ui/core";
import useStyles from "styles/RecentItemPageStyle";
import Buttons from "components/common/Buttons";

export default function NoItemTemplate({
  title,
  subtitle,
  buttontext,
  buttonUrl,
}) {
  const classes = useStyles();
  return (
    <Box className={classes.mobileNoItemBox}>
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
      <Buttons
        text={buttontext}
        onClick={(e) => {
          console.log("hello");
        }}
      ></Buttons>
    </Box>
  );
}
