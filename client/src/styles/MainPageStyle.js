import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    mobileRoot: {
      textAlign: "center",
      padding: theme.spacing(1),
      flexGrow: 1,
    },
    mobileRecommendMessageBox: {
      height: "6vh",
      textAlign: "left",
    },
    mobileRecommendMessage: {
      fontSize: "18px",
      fontWeight: "bold",
      color: "var(--color-black)"
    },
    mobileRecommendInfoBox: {
      height: "34vh",
    },
    mobileRecommendImageBox: {
      padding: "10px",
    },
    mobileImageBox: {
      height: "34vh",
      borderRadius: "15px",
      borderColor: "black",
      marginBottom: "10px"
    },
  
    // mobileImage: {
    //   objectFit: "cover",
    //   height: "100%",
    //   width: "100%",
    //   borderRadius: "15px",
    // },
    mobileImage: {
      objectFit: "cover",
      height: "100%",
      width: "100%",
      borderRadius: "15px",
    },
    mobileRecommendTextBox: {
      padding: "10px",
      textAlign: "left",
    },
    mobileBrandFavoriteBox: {
      height: "30px",
      display: "flex",
      justifyContent: "space-between",
    },
    mobileBrandName: {
      fontWeight: "bold",
      fontSize: "18px",
      color: "var(--color-black)",
    },
    mobileDescription: {
      height: "60%",
      color: "var(--color-gray)",
    },
    mobileShortDescription:{
      overflow: "hidden",
      whiteSpace: "nowrap",
      textOverflow: "ellipsis",
      color: "var(--color-gray)"
    },
    mobileDiscountPriceBox: {
      display: "flex",
      justifyContent: "space-between",
      fontSize: "25px",
    },
    mobileDiscount: {
      fontWeight: "bold",
      color: "var(--color-red)",
    },
    mobilePrice: {
      fontWeight:"bold",
      color: "var(--color-black)"
    },
    mobileCategoryContainer: {
        display: "flex",
        height: "8vh",
        borderTop: "1px solid #E0E3DA",
        borderBottom: "1px solid #E0E3DA",
        whiteSpace: "nowrap",
        overflowX: "auto",
        overflowY: "hidden"
    },
    mobileCategoryButton: {
        border: "1px solid var(--color-bg-dark)",
        borderRadius: "15px",
        margin: "10px 6px",
        backgroundColor: "var(--color-bg-dark)",
        fontWeight: "700",
        fontSize: "14px",
        paddingTop: "2px",
        paddingBottom: "2px",
        "&:hover, &:focus, &:active": {
            backgroundColor: "var(--color-main-b)",
            color: "var(--color-main-c)"
          },
    },
    mobileCategoryActiveButton: {
      border: "1px solid var(--color-main-b)",
      borderRadius: "15px",
      margin: "10px 6px",
      backgroundColor: "var(--color-main-b)",
      color: "var(--color-main-c)",
      fontWeight: "700",
      fontSize: "14px",
      paddingTop: "2px",
      paddingBottom: "2px",
      "&:hover, &:focus, &:active": {
        backgroundColor: "var(--color-main-b)",
        color: "var(--color-main-c)"
      },
    }
  }));


export default useStyles;