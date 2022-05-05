#include <stdbool.h>
#include <pixman.h>
#include <boost/python/module.hpp>
#include <boost/python/class.hpp>
#include <boost/python/scope.hpp>
#include "obj.h"

using namespace boost::python;

int getVals(py_DisplaySurface f, int index)
{
    return pixman_image_get_data(f.image)[index];
}
int get_format(py_DisplaySurface f)
{
    return pixman_image_get_format(f.image);
}
int get_width(py_DisplaySurface f)
{
    return pixman_image_get_width(f.image);
}
int get_height(py_DisplaySurface f)
{
    return pixman_image_get_height(f.image);
}
int get_stride(py_DisplaySurface f)
{
    return pixman_image_get_stride(f.image);
}
int get_depth(py_DisplaySurface f)
{
    return pixman_image_get_depth(f.image);
}
BOOST_PYTHON_MODULE(qemu_obj)
{
    class_<py_DisplaySurface>("py_DisplaySurface")
        .def("getVals", &getVals)
        .def("getFormat", &get_format)
        .def("getWidth", &get_width)
        .def("getHeight", &get_height)
        .def("getStride", &get_stride)
        .def("getDepth", &get_depth);

    class_<struct py_QemuDmaBuf>("py_QemuDmaBuf")
        .def_readonly("fd", &py_QemuDmaBuf::fd)
        .def_readonly("width", &py_QemuDmaBuf::width)
        .def_readonly("height", &py_QemuDmaBuf::height)
        .def_readonly("stride", &py_QemuDmaBuf::stride)
        .def_readonly("fourcc", &py_QemuDmaBuf::fourcc)
        .def_readonly("modifier", &py_QemuDmaBuf::modifier)
        .def_readonly("texture", &py_QemuDmaBuf::texture)
        .def_readonly("x", &py_QemuDmaBuf::x)
        .def_readonly("y", &py_QemuDmaBuf::y)
        .def_readonly("scanout_width", &py_QemuDmaBuf::scanout_width)
        .def_readonly("scanout_height", &py_QemuDmaBuf::scanout_height)
        .def_readonly("y0_top", &py_QemuDmaBuf::y0_top)
        .def_readonly("fence_fd", &py_QemuDmaBuf::fence_fd)
        .def_readonly("allow_fences", &py_QemuDmaBuf::allow_fences)
        .def_readonly("draw_submitted", &py_QemuDmaBuf::draw_submitted);

    class_<struct py_ScanoutTexture>("py_ScanoutTexture")
        .def_readonly("backing_id", &py_ScanoutTexture::backing_id)
        .def_readonly("backing_y_0_top", &py_ScanoutTexture::backing_y_0_top)
        .def_readonly("backing_width", &py_ScanoutTexture::backing_width)
        .def_readonly("x", &py_ScanoutTexture::x)
        .def_readonly("y", &py_ScanoutTexture::y)
        .def_readonly("width", &py_ScanoutTexture::width)
        .def_readonly("height", &py_ScanoutTexture::height);

    class_<struct py_QemuUIInfo>("py_QemuUIInfo")
        .def_readonly("width_mm", &py_QemuUIInfo::width_mm)
        .def_readonly("height_mm", &py_QemuUIInfo::height_mm)
        .def_readonly("xoff", &py_QemuUIInfo::xoff)
        .def_readonly("yoff", &py_QemuUIInfo::yoff)
        .def_readonly("width", &py_QemuUIInfo::width)
        .def_readonly("height", &py_QemuUIInfo::height);

    class_<struct py_QEMUGLParams>("py_QEMUGLParams")
        .def_readonly("major_ver", &py_QEMUGLParams::major_ver)
        .def_readonly("minor_ver", &py_QEMUGLParams::minor_ver);

    class_<struct py_USBDevice>("py_USBDevice")
        .def_readonly("port_path", &py_USBDevice::port_path)
        .def_readonly("serial", &py_USBDevice::serial)
        .def_readonly("flags", &py_USBDevice::flags)
        .def_readonly("pcap_filename", &py_USBDevice::pcap_filename)
        .def_readonly("speed", &py_USBDevice::speed)
        .def_readonly("speedmask", &py_USBDevice::speedmask)
        .def_readonly("addr", &py_USBDevice::addr)
        // .def_readonly("product_desc", &py_USBDevice::product_desc)
        .def_readonly("auto_attach", &py_USBDevice::auto_attach)
        .def_readonly("attached", &py_USBDevice::attached)
        .def_readonly("state", &py_USBDevice::state)
        // .def_readonly("setup_buf", &py_USBDevice::setup_buf)
        // .def_readonly("data_buf", &py_USBDevice::data_buf)
        .def_readonly("remote_wakeup", &py_USBDevice::remote_wakeup)
        .def_readonly("setup_state", &py_USBDevice::setup_state)
        .def_readonly("setup_len", &py_USBDevice::setup_len)
        .def_readonly("setup_index", &py_USBDevice::setup_index)
        .def_readonly("configuration", &py_USBDevice::configuration)
        .def_readonly("ninterfaces", &py_USBDevice::ninterfaces)
        // .def_readonly("altsetting)", &py_USBDevice::altsetting)
        ;
    class_<struct py_QEMUCursor>("py_QEMUCursor")
        .def_readonly("width", &py_QEMUCursor::width)
        .def_readonly("height", &py_QEMUCursor::height)
        .def_readonly("hot_x", &py_QEMUCursor::hot_x)
        .def_readonly("hot_y", &py_QEMUCursor::hot_y)
        .def_readonly("refcount", &py_QEMUCursor::refcount);

    class_<struct py_QemuDmaBuf>("py_QemuDmaBuf")
        .def_readonly("fd", &py_QemuDmaBuf::fd)
        .def_readonly("width", &py_QemuDmaBuf::width)
        .def_readonly("height", &py_QemuDmaBuf::height)
        .def_readonly("stride", &py_QemuDmaBuf::stride)
        .def_readonly("fourcc", &py_QemuDmaBuf::fourcc)
        .def_readonly("modifier", &py_QemuDmaBuf::modifier)
        .def_readonly("texture", &py_QemuDmaBuf::texture)
        .def_readonly("x", &py_QemuDmaBuf::x)
        .def_readonly("scanout_width", &py_QemuDmaBuf::scanout_width)
        .def_readonly("scanout_height", &py_QemuDmaBuf::scanout_height)
        .def_readonly("y0_top", &py_QemuDmaBuf::y0_top)
        .def_readonly("fence_fd", &py_QemuDmaBuf::fence_fd)
        .def_readonly("allow_fences", &py_QemuDmaBuf::allow_fences)
        .def_readonly("draw_submitted", &py_QemuDmaBuf::draw_submitted);

    class_<struct py_TextAttributes>("py_TextAttributes")
        .def_readonly("fgcol", &py_TextAttributes::fgcol)
        .def_readonly("bgcol", &py_TextAttributes::bgcol)
        .def_readonly("bold", &py_TextAttributes::bold)
        .def_readonly("uline", &py_TextAttributes::uline)
        .def_readonly("blink", &py_TextAttributes::blink)
        .def_readonly("invers", &py_TextAttributes::invers)
        .def_readonly("unvisible", &py_TextAttributes::unvisible);

    class_<struct py_DisplayChangeListener>("py_DisplayChangeListener")
        .def_readonly("update_interval", &py_DisplayChangeListener::update_interval)
        .def_readonly("bgcol", &py_DisplayChangeListener::ds)
        .def_readonly("bold", &py_DisplayChangeListener::con);

    class_<struct py_DisplayState>("py_DisplayState")
        .def_readonly("last_update", &py_DisplayState::last_update)
        .def_readonly("update_interval", &py_DisplayState::update_interval)
        .def_readonly("refreshing", &py_DisplayState::refreshing)
        .def_readonly("have_gfx", &py_DisplayState::have_gfx)
        .def_readonly("have_text", &py_DisplayState::have_text);

    class_<struct py_TextCell>("py_TextCell")
        .def_readonly("ch", &py_TextCell::ch)
        .def_readonly("t_attrib", &py_TextCell::t_attrib);

    class_<struct py_QemuConsole>("py_QemuConsole")
        .def_readonly("index", &py_QemuConsole::index)
        .def_readonly("console_type", &py_QemuConsole::console_type)
        .def_readonly("dcls", &py_QemuConsole::dcls)
        .def_readonly("gl_block", &py_QemuConsole::gl_block)
        .def_readonly("window_id", &py_QemuConsole::window_id)
        .def_readonly("width", &py_QemuConsole::head)
        .def_readonly("width", &py_QemuConsole::width)
        .def_readonly("total_height", &py_QemuConsole::total_height)
        .def_readonly("backscroll_height", &py_QemuConsole::backscroll_height)
        .def_readonly("x", &py_QemuConsole::x)
        .def_readonly("y", &py_QemuConsole::y)
        .def_readonly("t_attrib_default", &py_QemuConsole::t_attrib_default)
        .def_readonly("t_attrib", &py_QemuConsole::t_attrib)
        .def_readonly("x_saved", &py_QemuConsole::x_saved)
        .def_readonly("y_saved", &py_QemuConsole::y_saved)
        .def_readonly("y_displayed", &py_QemuConsole::y_displayed)
        .def_readonly("y_base", &py_QemuConsole::y_base)
        .def_readonly("cursor_invalidate", &py_QemuConsole::cursor_invalidate)
        .def_readonly("echo", &py_QemuConsole::echo)
        .def_readonly("update_x0", &py_QemuConsole::update_x0)
        .def_readonly("update_y0", &py_QemuConsole::update_y0)
        .def_readonly("update_x1", &py_QemuConsole::update_x1)
        .def_readonly("update_y1", &py_QemuConsole::update_y1)
        .def_readonly("state", &py_QemuConsole::state)
        .def_readonly("nb_esc_params", &py_QemuConsole::nb_esc_params);

    class_<struct py_USBDescriptor_device>("py_USBDescriptor_device")
        .def_readonly("bcdUSB_lo", &py_USBDescriptor_device::bcdUSB_lo)
        .def_readonly("bcdUSB_hi", &py_USBDescriptor_device::bcdUSB_hi)
        .def_readonly("bDeviceClass", &py_USBDescriptor_device::bDeviceClass)
        .def_readonly("bDeviceSubClass", &py_USBDescriptor_device::bDeviceSubClass)
        .def_readonly("bDeviceProtocol", &py_USBDescriptor_device::bDeviceProtocol)
        .def_readonly("bMaxPacketSize0", &py_USBDescriptor_device::bMaxPacketSize0)
        .def_readonly("idVendor_lo", &py_USBDescriptor_device::idVendor_lo)
        .def_readonly("idVendor_hi", &py_USBDescriptor_device::idVendor_hi)
        .def_readonly("idProduct_lo", &py_USBDescriptor_device::idProduct_lo)
        .def_readonly("idProduct_hi", &py_USBDescriptor_device::idProduct_hi)
        .def_readonly("bcdDevice_lo", &py_USBDescriptor_device::bcdDevice_lo)
        .def_readonly("bcdDevice_hi", &py_USBDescriptor_device::bcdDevice_hi)
        .def_readonly("iManufacturer", &py_USBDescriptor_device::iManufacturer)
        .def_readonly("iProduct", &py_USBDescriptor_device::iProduct)
        .def_readonly("iSerialNumber", &py_USBDescriptor_device::iSerialNumber)
        .def_readonly("bNumConfigurations", &py_USBDescriptor_device::bNumConfigurations);

    class_<struct py_USBDescriptor_device_qualifier>("py_USBDescriptor_device_qualifier")
        .def_readonly("bcdUSB_lo", &py_USBDescriptor_device_qualifier::bcdUSB_lo)
        .def_readonly("bcdUSB_hi", &py_USBDescriptor_device_qualifier::bcdUSB_hi)
        .def_readonly("bDeviceClass", &py_USBDescriptor_device_qualifier::bDeviceClass)
        .def_readonly("bDeviceSubClass", &py_USBDescriptor_device_qualifier::bDeviceSubClass)
        .def_readonly("bDeviceProtocol", &py_USBDescriptor_device_qualifier::bDeviceProtocol)
        .def_readonly("bMaxPacketSize0", &py_USBDescriptor_device_qualifier::bMaxPacketSize0)
        .def_readonly("bNumConfigurations", &py_USBDescriptor_device_qualifier::bNumConfigurations)
        .def_readonly("bReserved", &py_USBDescriptor_device_qualifier::bReserved);
    class_<struct py_USBDescriptor_config>("py_USBDescriptor_config")
        .def_readonly("wTotalLength_lo", &py_USBDescriptor_config::wTotalLength_lo)
        .def_readonly("wTotalLength_hi", &py_USBDescriptor_config::wTotalLength_hi)
        .def_readonly("bNumInterfaces", &py_USBDescriptor_config::bNumInterfaces)
        .def_readonly("bConfigurationValue", &py_USBDescriptor_config::bConfigurationValue)
        .def_readonly("iConfiguration", &py_USBDescriptor_config::iConfiguration)
        .def_readonly("bmAttributes", &py_USBDescriptor_config::bmAttributes)
        .def_readonly("bMaxPower", &py_USBDescriptor_config::bMaxPower);
    class_<struct py_USBDescriptor_interface>("py_USBDescriptor_interface")
        .def_readonly("bInterfaceNumber", &py_USBDescriptor_interface::bInterfaceNumber)
        .def_readonly("bNumEndpoints", &py_USBDescriptor_interface::bNumEndpoints)
        .def_readonly("bInterfaceClass", &py_USBDescriptor_interface::bInterfaceClass)
        .def_readonly("bInterfaceSubClass", &py_USBDescriptor_interface::bInterfaceSubClass)
        .def_readonly("bInterfaceProtocol", &py_USBDescriptor_interface::bInterfaceProtocol)
        .def_readonly("iInterface", &py_USBDescriptor_interface::iInterface);
    class_<struct py_USBDescriptor_endpoint>("py_USBDescriptor_endpoint")
        .def_readonly("bEndpointAddress", &py_USBDescriptor_endpoint::bEndpointAddress)
        .def_readonly("bmAttributes", &py_USBDescriptor_endpoint::bmAttributes)
        .def_readonly("wMaxPacketSize_lo", &py_USBDescriptor_endpoint::wMaxPacketSize_lo)
        .def_readonly("wMaxPacketSize_hi", &py_USBDescriptor_endpoint::wMaxPacketSize_hi)
        .def_readonly("bInterval", &py_USBDescriptor_endpoint::bInterval)
        .def_readonly("bRefresh", &py_USBDescriptor_endpoint::bRefresh)
        .def_readonly("bSynchAddress", &py_USBDescriptor_endpoint::bSynchAddress);
    class_<struct py_USBDescriptor_bos_super>("py_USBDescriptor_bos_super")
        .def_readonly("wTotalLength_lo", &py_USBDescriptor_bos_super::wTotalLength_lo)
        .def_readonly("wTotalLength_hi", &py_USBDescriptor_bos_super::wTotalLength_hi)
        .def_readonly("bNumDeviceCaps", &py_USBDescriptor_bos_super::bNumDeviceCaps)

        .def_readonly("bmAttributes", &py_USBDescriptor_bos_super::bmAttributes)
        .def_readonly("wSpeedsSupported_lo", &py_USBDescriptor_bos_super::wSpeedsSupported_lo)
        .def_readonly("wSpeedsSupported_hi", &py_USBDescriptor_bos_super::wSpeedsSupported_hi)
        .def_readonly("bFunctionalitySupport", &py_USBDescriptor_bos_super::bFunctionalitySupport)
        .def_readonly("bU1DevExitLat", &py_USBDescriptor_bos_super::bU1DevExitLat)
        .def_readonly("wU2DevExitLat_lo", &py_USBDescriptor_bos_super::wU2DevExitLat_lo)
        .def_readonly("wU2DevExitLat_hi", &py_USBDescriptor_bos_super::wU2DevExitLat_hi);
    class_<struct py_USBDescriptor_bos_usb2_ext>("py_USBDescriptor_bos_usb2_ext")
        .def_readonly("wTotalLength_lo", &py_USBDescriptor_bos_usb2_ext::wTotalLength_lo)
        .def_readonly("wTotalLength_hi", &py_USBDescriptor_bos_usb2_ext::wTotalLength_hi)
        .def_readonly("bNumDeviceCaps", &py_USBDescriptor_bos_usb2_ext::bNumDeviceCaps)

        .def_readonly("wTotalLength_lo", &py_USBDescriptor_bos_usb2_ext::wTotalLength_lo)
        .def_readonly("wTotalLength_hi", &py_USBDescriptor_bos_usb2_ext::wTotalLength_hi)
        .def_readonly("bNumDeviceCaps", &py_USBDescriptor_bos_usb2_ext::bNumDeviceCaps);

    class_<struct py_USBDescID>("py_USBDescID")
        .def_readonly("idVendor", &py_USBDescID::idVendor)
        .def_readonly("idProduct", &py_USBDescID::idProduct)
        .def_readonly("bcdDevice", &py_USBDescID::bcdDevice)
        .def_readonly("iManufacturer", &py_USBDescID::iManufacturer)
        .def_readonly("iProduct", &py_USBDescID::iProduct)
        .def_readonly("iSerialNumber", &py_USBDescID::iSerialNumber);

    class_<struct py_USBDescDevice>("py_USBDescDevice")
        .def_readonly("bcdUSB", &py_USBDescDevice::bcdUSB)
        .def_readonly("bDeviceClass", &py_USBDescDevice::bDeviceClass)
        .def_readonly("bDeviceSubClass", &py_USBDescDevice::bDeviceSubClass)
        .def_readonly("bDeviceProtocol", &py_USBDescDevice::bDeviceProtocol)
        .def_readonly("bMaxPacketSize0", &py_USBDescDevice::bMaxPacketSize0)
        .def_readonly("bNumConfigurations", &py_USBDescDevice::bNumConfigurations)
        .def_readonly("confs", &py_USBDescDevice::confs);

    class_<struct py_USBDescIfaceAssoc>("py_USBDescIfaceAssoc")
        .def_readonly("bFirstInterface", &py_USBDescIfaceAssoc::bFirstInterface)
        .def_readonly("bInterfaceCount", &py_USBDescIfaceAssoc::bInterfaceCount)
        .def_readonly("bFunctionClasfs", &py_USBDescIfaceAssoc::bFunctionClasfs)
        .def_readonly("bFunctionSubClass", &py_USBDescIfaceAssoc::bFunctionSubClass)
        .def_readonly("bFunctionProtocol", &py_USBDescIfaceAssoc::bFunctionProtocol)
        .def_readonly("iFunction", &py_USBDescIfaceAssoc::iFunction)
        .def_readonly("nif", &py_USBDescIfaceAssoc::nif)
        .def_readonly("ifs", &py_USBDescIfaceAssoc::ifs);
    class_<struct py_USBDescIface>("py_USBDescIface")
        .def_readonly("bInterfaceNumber", &py_USBDescIface::bInterfaceNumber)
        .def_readonly("bAlternateSetting", &py_USBDescIface::bAlternateSetting)
        .def_readonly("bNumEndpoints", &py_USBDescIface::bNumEndpoints)
        .def_readonly("bInterfaceSubClass", &py_USBDescIface::bInterfaceSubClass)
        .def_readonly("bInterfaceProtocol", &py_USBDescIface::bInterfaceProtocol)
        .def_readonly("iInterface", &py_USBDescIface::iInterface)
        .def_readonly("ndesc", &py_USBDescIface::ndesc)
        .def_readonly("descs", &py_USBDescIface::descs)
        .def_readonly("eps", &py_USBDescIface::eps);
    class_<struct py_USBDescEndpoint>("py_USBDescEndpoint")
        .def_readonly("bEndpointAddress", &py_USBDescEndpoint::bEndpointAddress)
        .def_readonly("bmAttributes", &py_USBDescEndpoint::bmAttributes)
        .def_readonly("wMaxPacketSize", &py_USBDescEndpoint::wMaxPacketSize)
        .def_readonly("bInterval", &py_USBDescEndpoint::bInterval)
        .def_readonly("bRefresh", &py_USBDescEndpoint::bRefresh)
        .def_readonly("bSynchAddress", &py_USBDescEndpoint::bSynchAddress)
        .def_readonly("is_audio", &py_USBDescEndpoint::is_audio)
        .def_readonly("extra", &py_USBDescEndpoint::extra)
        .def_readonly("bSynchAddress", &py_USBDescEndpoint::bSynchAddress)
        .def_readonly("bMaxBurst", &py_USBDescEndpoint::bMaxBurst)
        .def_readonly("bmAttributes_super", &py_USBDescEndpoint::bmAttributes_super)
        .def_readonly("wBytesPerInterval", &py_USBDescEndpoint::wBytesPerInterval);
    class_<struct py_USBDescOther>("py_USBDescOther")
        .def_readonly("length", &py_USBDescOther::length)
        .def_readonly("data", &py_USBDescOther::data);
    class_<struct py_USBDescMSOS>("py_USBDescMSOS")
        .def_readonly("CompatibleID", &py_USBDescMSOS::CompatibleID)
        .def_readonly("Label", &py_USBDescMSOS::Label)
        .def_readonly("SelectiveSuspendEnabled", &py_USBDescMSOS::SelectiveSuspendEnabled);
    class_<struct py_USBDesc>("py_USBDesc")
        .def_readonly("id", &py_USBDesc::id)
        // .def_readonly("full", &py_USBDesc::full)
        // .def_readonly("high", &py_USBDesc::high)
        // .def_readonly("super", &py_USBDesc::super)
        .def_readonly("str", &py_USBDesc::str)
        .def_readonly("msos", &py_USBDesc::msos);
    class_<struct py_NetPacket>("py_NetPacket")
        .def_readonly("flags", &py_NetPacket::flags)
        .def_readonly("size", &py_NetPacket::size)
        .def_readonly("data", &py_NetPacket::data);
    class_<struct py_NetQueue>("py_NetQueue");
    class_<struct py_NetClientState>("py_NetClientState");
    class_<struct py_NetQueue>("py_NetQueue");
    class_<struct py_NetClientState>("py_NetClientState");
    class_<struct py_NICPeers>("py_NICPeers");
    class_<struct py_NICConf>("py_NICConf");
    class_<struct py_NetFilterState>("py_NetFilterState");
    class_<struct py_NICState>("py_NICState");
    class_<struct py_NICConf>("py_NICConf");
}

// char *QEMUCursor_(QEMUCursor *dmabuf)
// {
// return "hello, world";
// }
BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
}
