import React, { useState } from "react";
import axios from "axios";
import { Box, Grid } from "@material-ui/core";
import { useStyles } from "../../styles/ImageUploadPageStyles";
import AddCircleOutlineRoundedIcon from "@material-ui/icons/AddCircleOutlineRounded";

export default function UploadImageComponent({ src, inputtype, user_id }) {
    const classes = useStyles();
    const [image, setImage] = useState();
  
    function PostImage() {
      const formData = new FormData();
      axios.post(
        `${process.env.REACT_APP_API_URL}/imgupload/${user_id}`,
        formData,
        {
          headers: { Authorization: "Bearer " + localStorage.getItem("jwt") },
        }
      );
    }
  
    function DeleteImage() {
      axios.delete(`${process.env.REACT_APP_API_URL}/imgupload/${user_id}`, {
        headers: { Authorization: "Bearer " + localStorage.getItem("jwt") },
      });
    }
  
    function onChangeImage(e) {
      setImage(e.target.files[0]);
      console.log(e.target.files[0]);
  
      const formData = new FormData();
      formData.append("file", image);
      // 서버의 upload API 호출
      PostImage();
    }
  
    if (inputtype !== "empty") {
      return (
        <Grid
          className={classes.mobileClosetImageGrid}
          inputtype={inputtype}
          onClick={() => {
            console.log("popup delete modal");
            // DeleteImage()
          }}
          item
          xs={4}
        >
          <Grid container className={classes.mobileEmptyImageBox}>
            <img className={classes.mobileImage} src={src} alt="none" />
          </Grid>
        </Grid>
      );
    } else {
      return (
        <Grid
          className={classes.mobileClosetImageGrid}
          inputtype={inputtype}
          item
          xs={4}
          onClick={() => {
            console.log("addimage");
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
                action="upload"
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