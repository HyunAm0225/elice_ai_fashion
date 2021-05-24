import React from "react";
import { Box, Typography } from "@material-ui/core";
import useStyles from "../../styles/RecentItemPageStyle";
import Buttons from "../common/Buttons";

export default function NoItemTemplate({ title, subtitle, buttontext, buttonUrl }) {
  const classes = useStyles();
  return (
    <React.Fragment>
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
        <Buttons text={buttontext}></Buttons>
      </Box>
    </React.Fragment>
  );
}
