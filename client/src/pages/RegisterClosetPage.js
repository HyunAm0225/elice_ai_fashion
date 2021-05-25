import React from "react";
import { Mobile } from "../MediaQuery";
import { Box, Button } from "@material-ui/core";
import useStyles from "../styles/AuthPageStyle";
import Navbar from "../components/common/Navbar";

function RegisterPage() {
  const classes = useStyles();
  const title = "닉네임님의 클로젯";
  const message = "~~~~~~~~~이미지를 분석해서 아이템을 추천해줄거에요";

  return (
    <Mobile>
      <Navbar />
      <Box className={classes.mobileAuthBox}>
        <Box>
          <Box className={classes.mobileTextBox}>
            <Box className={classes.mobileTitle}>{title}</Box>
            <Box className={classes.mobileControlBox}></Box>
            <Box className={classes.mobileMessage}>{message}</Box>
          </Box>
          <Box className={classes.mobileButtonBox}>
            <Button
              className={classes.mobileButton}
              variant="contained"
              onClick={() => {}}
            >
              지금 추가하기
            </Button>
          </Box>
        </Box>
      </Box>
    </Mobile>
  );
}

export default RegisterPage;
