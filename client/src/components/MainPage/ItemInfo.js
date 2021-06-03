import React from "react";
import { Grid, Box } from "@material-ui/core";
import FavoriteIcon from "components/MainPage/FavoriteIcon";
import useStyles from "styles/MainPageStyle";

export default function ItemInfo({ idx, data }) {
  const classes = useStyles();
  return (
    <Grid className="mobileSmallPaddingBox" item xs={6}>
      <Box className={classes.mobileItemImageBox}>
        <img className="mobileImage" src={data["thumnail"]} alt="옷"></img>
      </Box>
      <Box className={classes.mobileItemDiscountPriceBox}>
        <Box className={classes.mobileItemDiscount}>
          {data["discount_rate"]}%
        </Box>
        <Box className={classes.mobileItemPrice}>{data["sale_price"]}$</Box>
      </Box>
      <Box className={classes.mobileItemBrandFavoriteBox}>
        <Box className={classes.mobileItemBrandName}>
          <a href={data["url"]}>{data["brand"]}</a>
        </Box>
        <FavoriteIcon idx={idx.toString()} />
      </Box>
      <Box className={classes.mobileItemShortDescription}>{data["name"]}</Box>
    </Grid>
  );
}
