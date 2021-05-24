import { Box } from "@material-ui/core";
import useStyles from "../../styles/MyPageStyle";

function Shopping() {
  const classes = useStyles();

  return (
    <Box item className={classes.mobileShoppingBox}>
      <Box className={classes.mobileBoldText}>쇼핑</Box>
      <Box>최근 본 상품</Box>
      <Box>찜한 상품</Box>
    </Box>
  );
}

export default Shopping;
