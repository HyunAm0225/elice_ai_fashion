import React, { useState, useEffect } from "react";
import { Box, Grid } from "@material-ui/core";
import { Mobile } from "MediaQuery";
import useStyles from "styles/RecentItemPageStyle";
import { Loader } from "components/common/Loader";
import Navbar from "components/common/Navbar";
import Infinite from "components/common/Infinite";
import TextTitleComponent from "components/SimilarItemPage/TextTitleComponent";
import NoItemTemplate from "components/SimilarItemPage/NoItemTemplate";
import axios from "axios";

export default function RecentItemPage() {
  const classes = useStyles();
  const [dataList, setDataList] = useState([1, 2, 3, 4, 5, 6]);
  const [info, setInfo] = useState([]);

  // 최근 본 상품 출력(코드 수정해야함)
  useEffect(() => {
    (async function () {
      await axios
        .get(`${process.env.REACT_APP_API_URL}/api/fashion`)
        .then((response) => {
          setInfo(response.data);
        });
    })();
  }, []);

  if (dataList.length > 0) {
    return (
      <Mobile>
        <Navbar />
        <TextTitleComponent
          title="최근 본 상품"
          number={info && info.length ? info.length : ""}
        />
        <Grid className="mobileRoot">
          <Grid container>
            {info && info.length ? <Infinite info={info} /> : <Loader />}
          </Grid>
        </Grid>
      </Mobile>
    );
  } else {
    return (
      <Mobile>
        <Box className={classes.mobileContainer}>
          <Navbar />
          <Box className={classes.mobileEmptyBox} />
          <NoItemTemplate
            title="최근에 본 상품이 없어요"
            subtitle="클릭하시면 비슷한 상품을 모아서 볼 수 있어요"
            buttontext="클로젯 추가하기"
            buttonUrl=""
          />
        </Box>
      </Mobile>
    );
  }
}
