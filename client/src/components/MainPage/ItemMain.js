import { Grid, Box } from "@material-ui/core";
import useStyles from "../../styles/MainPageStyle";
import FavoriteIcon from "./FavoriteIcon";

export default function ItemMain({ idx }) {
  const classes = useStyles();
  const title = "당신(닉네임) 만을 위한 추천 아이템 :)";
  const brand = "노드스트롬";
  const description = "Zella Live In High Walst Pocket 7/8 Leggings";
  const discount = "33%";
  const price = "57,300";

  return (
    <Grid className={classes.mobileRoot}>
      <Grid className={classes.mobileRecommendMessageBox}>
        <Box className={classes.mobileRecommendMessage}>{title}</Box>
      </Grid>
      <Grid container className={classes.mobileRecommendInfoBox}>
        <Grid className={classes.mobileRecommendImageBox} item xs={6}>
          <img
            className={classes.mobileImage}
            src="http://fpost.co.kr/board/data/editor/1902/af6295e29b76e6d52de0accea62b4e4b_1550713144_4274.jpg"
            alt="clothes"
          />
        </Grid>
        <Grid className={classes.mobileRecommendTextBox} item xs={6}>
          <Box className={classes.mobileBrandFavoriteBox}>
            <Box className={classes.mobileBrandName}>{brand}</Box>
            <FavoriteIcon idx={"0"} />
          </Box>
          <Box className={classes.mobileDescription}>{description}</Box>
          <Box className={classes.mobileDiscountPriceBox}>
            <Box className={classes.mobileDiscount}>{discount}</Box>
            <Box className={classes.mobilePrice}>{price}</Box>
          </Box>
        </Grid>
      </Grid>
    </Grid>
  );
}
