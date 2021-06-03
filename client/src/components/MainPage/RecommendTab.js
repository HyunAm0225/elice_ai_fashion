import React, { useState, useEffect } from "react";
import { Box } from "@material-ui/core";
import useStyles from "styles/MainPageStyle";
import ItemMain from "components/MainPage/ItemMain";

export default function RecommendTab() {
  const classes = useStyles();
  const [images, setImages] = useState([]);
  const [count, setCount] = useState(1);

  const fetchImages = (cnt) => {
    setImages([...images, cnt, cnt + 1, cnt + 2, cnt + 3]);
    setCount(cnt + 4);
  };

  useEffect(() => {
    fetchImages(count);
  }, []);

  return (
    <Box className={classes.mobileRecommendContainer}>
      {images.map((idx) => (
        <ItemMain key={idx} idx={idx} />
      ))}
    </Box>
  );
}
