import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  // LikeItemPage, RecentItemPage
  mobileContainer: {
    height: "auto",
    position: "relative",
    justifyContent: "center",
    alignContent: "center",
  },
  mobileEmptyBox: {
    height: "35vh",
  },
  // TextTitleComponent
  mobileTitleBox: {
    margin: "10px",
    marginBottom: "50px",
  },
  mobileTitleText: {
    fontWeight: "bold",
    fontSize: "21px",
  },
  mobileSubtitleText: {
    color: "rgba(165, 147, 224, 1)",
    fontSize: "15px",
  },
  // NoItemTemplate
  mobileNoItemBox: {
    textAlign: "center",
  },
}));

export default useStyles;
