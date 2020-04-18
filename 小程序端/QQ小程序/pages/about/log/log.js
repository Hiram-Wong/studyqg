const app = getApp();
Page({
  data: {
    arryList: [],
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    ColorList: app.globalData.ColorList,    
  },
  onLoad: function () { 
    var that = this;
    wx.request({
      method: 'GET',
      url: 'https://study.catni.cn/log',
      success:function(res){
        console.log(res);
        that.setData({
          arryList: res.data
        });

        // console.log(that.arryList.length)
      }
    })
    console.log(this.arryList)
  },
  pageBack() {
    wx.navigateBack({
      delta: 1
    });
  },
  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  // 获取滚动条当前位置
  onPageScroll: function (e) {
    console.log(e)
    if (e.scrollTop > 100) {
      this.setData({
        floorstatus: true
      });
    } else {
      this.setData({
        floorstatus: false
      });
    }
  },

  //回到顶部
  goTop: function (e) {  // 一键回到顶部
    if (wx.pageScrollTo) {
      wx.pageScrollTo({
        scrollTop: 0
      })
    } else {
      wx.showModal({
        title: '提示',
        content: '当前微信版本过低，无法使用该功能，请升级到最新微信版本后重试。'
      })
    }
  }
});
