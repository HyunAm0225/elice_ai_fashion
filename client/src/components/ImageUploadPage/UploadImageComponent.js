import React, { useEffect, useState } from "react";
import axios from "axios";
import { Box, Grid } from "@material-ui/core";
import { useStyles } from "styles/ImageUploadPageStyles";
import AddCircleOutlineRoundedIcon from "@material-ui/icons/AddCircleOutlineRounded";

export default function UploadImageComponent({ src, inputtype, user_id }) {
  const classes = useStyles();
  const [image, setImage] = useState(null);

  function onChangeImage(e) {
    e.preventDefault();
    setImage(e.target.files[0]);
    console.log(image, "이미지 업로드 된거 체크");
  }

  // 업로드 이미지 백엔드 전송
  useEffect(() => {
    if (image !== null) {
      const formData = new FormData();
      formData.append("dress_img", image);
      formData.append("user_id", localStorage.getItem("user"));
      axios.post(`${process.env.REACT_APP_API_URL}/api/closet/`, formData, {
        headers: { Authorization: "JWT " + localStorage.getItem("jwt") },
        "content-type": "multipart/form-data",
      });
    }
  }, [image]);

  if (inputtype !== "empty") {
    return (
      <Grid
        className="mobileSmallPaddingBox"
        inputtype={inputtype}
        onClick={() => {
          console.log("popup delete modal");
        }}
        item
        xs={4}
      >
        <Grid container className={classes.mobileEmptyImageBox}>
          <img className="mobileImage" src={src} alt="none" />
        </Grid>
      </Grid>
    );
  } else {
    return (
      <Grid
        className="mobileSmallPaddingBox"
        inputtype={inputtype}
        item
        xs={4}
        onClick={(e) => {
          document.all.file.click();
        }}
      >
        <Grid
          container
          inputtype={inputtype}
          className={classes.mobileEmptyImageBox}
        >
          <Box>
            <form
              action="/"
              id="uploadForm"
              method="post"
              enctype="multipart/form-data"
            >
              <input
                type="file"
                name="file"
                id="file"
                className={classes.mobileInput}
                onChange={onChangeImage}
              />
            </form>
            <AddCircleOutlineRoundedIcon
              className={classes.mobileEmptyImageIcon}
            />
          </Box>
        </Grid>
      </Grid>
    );
  }
}
