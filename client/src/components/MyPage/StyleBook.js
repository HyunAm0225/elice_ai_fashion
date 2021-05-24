import { Grid, Box } from "@material-ui/core";
import useStyles from "../../styles/MyPageStyle";

function StyleBook() {
  const classes = useStyles();
  const imagePath =
    "http://fpost.co.kr/board/data/editor/1902/af6295e29b76e6d52de0accea62b4e4b_1550713144_4274.jpg";

  return (
    <Box item className={classes.mobileStyleBookBox}>
      <Box className={classes.mobileStyleBookText}>나의 스타일북</Box>
      <Grid container className={classes.mobileStyleImageBox}>
        <Grid className={classes.mobileSmallPadding} item xs={4}>
          <img className={classes.mobileImage} src={imagePath} alt="clothes" />
        </Grid>
        <Grid className={classes.mobileSmallPadding} item xs={4}>
          <img className={classes.mobileImage} src={imagePath} alt="clothes" />
        </Grid>
        <Grid className={classes.mobileSmallPadding} item xs={4}>
          <img className={classes.mobileImage} src={imagePath} alt="clothes" />
        </Grid>
      </Grid>
    </Box>
  );
}

export default StyleBook;
