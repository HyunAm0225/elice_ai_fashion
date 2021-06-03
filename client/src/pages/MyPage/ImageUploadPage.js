import React, { useState, useEffect } from "react";
import axios from "axios";
import { Box, Grid } from "@material-ui/core";
import { Mobile } from "MediaQuery";
import Navbar from "components/common/Navbar";
import { useStyles } from "styles/ImageUploadPageStyles";
import TextTitleComponent from "components/ImageUploadPage/TextTitleComponent";
import UploadImageComponent from "components/ImageUploadPage/UploadImageComponent";
import { useHistory } from "react-router-dom";

export default function ImageUploadPage({ match }) {
  const classes = useStyles();
  const user_id = match.params.user_id;
  const [imageData, setImageData] = useState(["1", "2", "3", "4"]);
  const [imageList, setImageList] = useState(null);
  const [image, setImage] = useState(null);

  // url을 통한 다른 사용자 접근 통제 필요
  const history = useHistory();
  if (localStorage.getItem("jwt") === null) {
    history.push("/login");
  }

  // get User Image 리스트
  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_API_URL}/api/closet/`, {
        headers: { Authorization: "JWT " + localStorage.getItem("jwt") },
      })
      .then((response) => {
        setImageData(response.data);
      });
  }, []);

  // User Image 데이터 기준으로 컴포넌트 생성
  useEffect(() => {
    if (imageData) {
      setImageList(
        imageData.map((data, idx) => (
          <UploadImageComponent
            src={data.dress_img}
            inputtype="image"
            user_id={user_id}
            id={idx}
          />
        )),
      );
    }
  }, [imageData]);

  return (
    <Mobile>
      <Box className={classes.mobileContainer}>
        <Navbar />
        <TextTitleComponent
          title="클로젯에 이미지를 추가해주시면 AI 분석을 통해서 아이템을 추천해드려요."
          subtitle="클릭하시면 사진 속 의상과 비슷한 상품을 모아서 볼 수 있어요."
        />
      </Box>
      <Grid container>
        {imageList}
        <UploadImageComponent inputtype="empty" user_id={user_id} />
      </Grid>
    </Mobile>
  );
}
