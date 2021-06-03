import { Box } from "@material-ui/core";
import useStyles from "styles/MyPageStyle";
import { Link } from "react-router-dom";

function Shopping() {
  const classes = useStyles();

  return (
    <Box item className={classes.mobileShoppingBox}>
      <Box className="mobileBoldText">쇼핑</Box>
      <Box
        component={Link}
        to={"/rcntitem"}
        className={classes.mobileShoppingText}
      >
        최근 본 상품
      </Box>
      <Box
        component={Link}
        to={"/likeitem"}
        className={classes.mobileShoppingText}
      >
        찜한 상품
      </Box>
    </Box>
  );
}

export default Shopping;
