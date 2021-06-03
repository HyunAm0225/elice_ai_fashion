import React, { useState } from "react";
import { Box, Grid } from "@material-ui/core";
import { Mobile } from "MediaQuery";
import useStyles from "styles/RecentItemPageStyle";
import Navbar from "components/common/Navbar";
import Infinite from "components/common/Infinite";
import TextTitleComponent from "components/SimilarItemPage/TextTitleComponent";
import NoItemTemplate from "components/SimilarItemPage/NoItemTemplate";

export default function SimilarItemPage() {
  const classes = useStyles();
  const [dataList, setDataList] = useState([]);

  if (dataList.length > 0) {
    return (
      <Mobile>
        <Navbar />
        <TextTitleComponent
          title="나의 클로젯 아이템과 비슷한 상품"
          number="3"
        />
        <Grid className="mobileRoot">
          <Grid container>
            <Infinite />
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
            title="비슷한 아이템이 아직 올라오지 않았어요!"
            subtitle="클릭하시면 비슷한 상품을 모아서 볼 수 있어요"
            buttontext="추천상품 보러가기"
            buttonUrl=""
          />
        </Box>
      </Mobile>
    );
  }
}
