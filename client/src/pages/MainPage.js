import React, { useEffect, useState } from "react";
import { Grid, Box } from "@material-ui/core";
import useStyles from "../styles/MainPageStyle";
import { Mobile } from "../MediaQuery";
import Navbar from "../components/common/Navbar";
import Infinite from "../components/MainPage/Infinite";
import Category from "../components/MainPage/Category";
import RecommendTab from "../components/MainPage/RecommendTab";
import axios from "axios";

export default function MainPage() {
  const classes = useStyles();
  const [username, setUsername] = useState("당신만");
  const [info, setInfo] = useState([]);

  useEffect(() => {
    (async function () {
      await axios
        .get(`${process.env.REACT_APP_API_URL}/api/fashion`)
        .then((response) => {
          setInfo(response.data);
        });
      if (localStorage.getItem("username") !== null) {
        setUsername(localStorage.getItem("username") + "님");
      }
    })();
  }, []);

  return (
    <Mobile>
      <Navbar />
      <Grid className={classes.mobileRoot}>
        <Box className={classes.mobileRecommendMessageBox}>
          <Box className={classes.mobileRecommendMessage}>
            <Box style={{ display: "flex", justifyContent: "space-between" }}>
              <Box>{username}을 위한 추천 아이템</Box>
              <Box style={{ fontSize: "12px", color: "var(--color-main-a)" }}>전체보기</Box>
            </Box>
          </Box>
        </Box>
        <RecommendTab />
        <Box className={classes.mobileRecommendMessageBox}>
          <Box className={classes.mobileRecommendMessage}>해외직구 상품</Box>
        </Box>
      </Grid>
      <Category />
      <Grid className={classes.mobileRoot}>
        <Grid container>
          {info && info.length ? <Infinite info={info} /> : null}
        </Grid>
      </Grid>
    </Mobile>
  );
}
