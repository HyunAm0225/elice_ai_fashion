import React, { useEffect, useState } from "react";
import { Grid } from "@material-ui/core";
import { Mobile } from "MediaQuery";
import useStyles from "styles/RecentItemPageStyle";
import { Loader } from "components/common/Loader";
import Navbar from "components/common/Navbar";
import Infinite from "components/common/Infinite";
import TextTitleComponent from "components/SimilarItemPage/TextTitleComponent";
import Category from "components/MainPage/Category";
import axios from "axios";

export default function RecommendItemPage() {
  const classes = useStyles();
  const [dataList, setDataList] = useState([]);
  const [info, setInfo] = useState([]);

  useEffect(() => {
    (async function () {
      await axios
        .get(`${process.env.REACT_APP_API_URL}/api/fashion`)
        .then((response) => {
          setInfo(response.data);
        });
    })();
  }, []);

  return (
    <Mobile>
      <Navbar />
      <TextTitleComponent title="''님을 위한 추천 아이템" number="3" />
      <Category />
      <Grid className="mobileRoot">
        <Grid container>
          {info && info.length ? <Infinite info={info} /> : <Loader />}
        </Grid>
      </Grid>
    </Mobile>
  );
}
