import { Grid, Box } from "@material-ui/core";
import useStyles from "styles/MainPageStyle";
import FavoriteIcon from "components/MainPage/FavoriteIcon";

export default function ItemMain({ idx }) {
  const classes = useStyles();
  const brand = "노드스트롬";
  const description = "Zella Live In High Walst Pocket 7/8 Leggings";
  const discount = "33%";
  const price = "57,300";

  return (
    <Grid container className="mobileGlassBox">
      <Grid className={classes.mobileRecommendImageBox} item xs={6}>
        <img
          className={classes.mobileRecommendImage}
          src="http://fpost.co.kr/board/data/editor/1902/af6295e29b76e6d52de0accea62b4e4b_1550713144_4274.jpg"
          alt="clothes"
        />
      </Grid>
      <Grid className={classes.mobileRecommendTextBox} item xs={6}>
        <Box className={classes.mobileBrandFavoriteBox}>
          <Box className={classes.mobileBrandName}>{brand}</Box>
          <FavoriteIcon idx={"0"} />
        </Box>
        <Box className={classes.mobileRecommendDescription}>{description}</Box>
        <Box className={classes.mobileRecommendDiscountPriceBox}>
          <Box className={classes.mobileRecommendDiscount}>{discount}</Box>
          <Box className={classes.mobileRecommendPrice}>{price}</Box>
        </Box>
        <Box>구매하기</Box>
      </Grid>
    </Grid>
  );
}
