import React, { useState } from "react";
import { Box, Button } from "@material-ui/core";
import useStyles from "styles/MainPageStyle";

export default function Category() {
  const classes = useStyles();
  const [activeButton, setActiveButton] = useState(0);

  const categories = [
    "전체",
    "높은 가격순",
    "낮은 가격순",
    "상의",
    "하의",
    "드레스",
    "스커트",
    "팬츠",
    "자켓",
  ].map((category, idx) =>
    activeButton === idx ? (
      <Button
        onClick={() => setActiveButton(idx)}
        className={classes.mobileCategoryActiveButton}
        key={idx}
      >
        {category}
      </Button>
    ) : (
      <Button
        onClick={() => setActiveButton(idx)}
        className={classes.mobileCategoryButton}
        key={idx}
      >
        {category}
      </Button>
    ),
  );

  return <Box className={classes.mobileCategoryContainer}>{categories}</Box>;
}
