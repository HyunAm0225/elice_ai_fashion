import React, { useEffect, useState } from "react";
import { Glow, Box } from "@material-ui/core";
import useStyles from "styles/MainPageStyle";
import { Mobile } from "MediaQuery";
import Navbar from "components/common/Navbar";
import axios from "axios";
import ProductBox from "components/common/ProductBox";
import SmallProductBox from "components/common/SmallProductBox";

import { useRecoilValue, useSetRecoilState, useRecoilState } from "recoil";
import { categoryState, pageState, countAllState } from "recoil/atoms";

export default function MainPage() {
  const classes = useStyles();
  const [username, setUsername] = useState("당신만");
  const [info, setInfo] = useState([]);
  const category = useRecoilValue(categoryState);
  const [page, setPage] = useRecoilState(pageState);
  const [countAll, setCountAll] = useRecoilState(countAllState);
  console.log("변수선언하는곳");

  // 메인페이지 접속시 모든 아이템 출력
  useEffect(() => {
    console.log("메인페이지 접속/카테고리 변경");
    if (category === "recommend") {
      (async function () {
        await axios
          .get(
            `${process.env.REACT_APP_API_URL}/api/recommend`, 
          )
          .then(async (response) => {
            console.log(response.data.count);
            console.log(response.data);
            setPage(1);
            setInfo(response.data.results);
            setCountAll(response.data.count);
          });
        if (localStorage.getItem("username") !== null) {
          setUsername(localStorage.getItem("username") + "님");
        }
      })();
    } else {
      (async function () {
        await axios
          .get(
            `${process.env.REACT_APP_API_URL}/api/fashion/?category=${category}`
          )
          .then(async (response) => {
            console.log(response.data.count);
            console.log(response.data);
            setPage(1);
            setInfo(response.data.results);
            setCountAll(response.data.count);
          });
        if (localStorage.getItem("username") !== null) {
          setUsername(localStorage.getItem("username") + "님");
        }
      })();
    }
  }, [category]);

  useEffect(() => {
    console.log("페이지 추가 ", page);
    if (page > 1) {
      (async function () {
        await axios
          .get(
            `${process.env.REACT_APP_API_URL}/api/fashion/?category=${category}&page=${page}`
          )
          .then((response) => {
            console.log(response.data.results);
            setInfo([...info, ...response.data.results]);
          });
      })();
    }
  }, [page]);

  return (
    <Mobile>
      <Box>
        <Navbar />
        <SmallProductBox title="당신이 찾고 있는 상품" />
        <SmallProductBox title="당신을 위한 추천 상품" />
        <ProductBox info={info} title={`해외직구 상품 ${countAll}`} navbar={true} />
      </Box>
    </Mobile>
  );
}