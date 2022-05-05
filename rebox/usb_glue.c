
#include "qemu/osdep.h"
#include "qapi/error.h"
#include "qemu/main-loop.h"
#include "qemu/module.h"
#include "hw/usb.h"
#include "usb_glue.h"

// USBDevice
// USBDevice *find_device(USBDevice *dev, uint8_t addr)
void glue_cancel_packet(USBDevice *dev, USBPacket *p)
{
}
void glue_handle_attach(USBDevice *dev)
{
}
void glue_handle_reset(USBDevice *dev)
{
}
void glue_handle_control(USBDevice *dev, USBPacket *p, int request, int value, int index, int length, uint8_t *data)
{
}
void glue_handle_data(USBDevice *dev, USBPacket *p)
{
}
void glue_set_interface(USBDevice *dev, int interface, int alt_old, int alt_new)
{
}
void glue_flush_ep_queue(USBDevice *dev, USBEndpoint *ep)
{
}
void glue_ep_stopped(USBDevice *dev, USBEndpoint *ep)
{
}
void glue_alloc_streams(USBDevice *dev, USBEndpoint **eps, int nr_eps, int streams)
{
}
void glue_free_streams(USBDevice *dev, USBEndpoint **eps, int nr_eps)
{
}

void glue_glue_dev(USBPort *port)
{
}
void glue_glue_detach(USBPort *port)
{
}
void glue_glue_child_detach(USBPort *port, USBDevice *child)
{
}
void glue_glue_wakeup(USBPort *port)
{
}
void glue_glue_complete(USBPort *port, USBPacket *p)
{
}

// USBPacket
void get_USBPacket_pid(void *s)
{
}
void get_USBPacket_id(void *s)
{
}
void get_USBPacket_ep(void *s)
{
}
void get_USBPacket_stream(void *s)
{
}
void get_USBPacket_iov(void *s)
{
}
void get_USBPacket_parameter(void *s)
{
}
void get_USBPacket_short_not_ok(void *s)
{
}
void get_USBPacket_int_req(void *s)
{
}
void get_USBPacket_status(void *s)
{
}
void get_USBPacket_actual_length(void *s)
{
}
void get_USBPacket_state(void *s)
{
}
void get_USBPacket_combined(void *s)
{
}
void get_USBPacket_queue(void *s)
{
}
void get_USBPacket_combined_entry(void *s)
{
}
// USBDevice
void *get_USBDevice_port_get()
{
}
void get_USBDevice_qdev(void *s)
{
}
void get_USBDevice_port(void *s)
{
}
void get_USBDevice_port_path(void *s)
{
}
void get_USBDevice_serial(void *s)
{
}
void get_USBDevice_opaque(void *s)
{
}
void get_USBDevice_flags(void *s)
{
}
void get_USBDevice_pcap_filename(void *s)
{
}
void get_USBDevice_pcap(void *s)
{
}
void get_USBDevice_speed(void *s)
{
}
void get_USBDevice_speedmask(void *s)
{
}
void get_USBDevice_addr(void *s)
{
}
void get_USBDevice_product_desc(void *s)
{
}
void get_USBDevice_auto_attach(void *s)
{
}
void get_USBDevice_attached(void *s)
{
}
void get_USBDevice_state(void *s)
{
}
void get_USBDevice_setup_buf(void *s)
{
}
void get_USBDevice_data_buf(void *s)
{
}
void get_USBDevice_remote_wakeup(void *s)
{
}
void get_USBDevice_setup_state(void *s)
{
}
void get_USBDevice_setup_len(void *s)
{
}
void get_USBDevice_setup_index(void *s)
{
}
void get_USBDevice_ep_ctl(void *s)
{
}
void get_USBDevice_ep_in(void *s)
{
}
void get_USBDevice_ep_out(void *s)
{
}
void get_USBDevice_strings(void *s)
{
}
void get_USBDevice_usb_desc(void *s)
{
}
void get_USBDevice_device(void *s)
{
}
void get_USBDevice_configuration(void *s)
{
}
void get_USBDevice_ninterfaces(void *s)
{
}
void get_USBDevice_altsetting(void *s)
{
}
void get_USBDevice_config(void *s)
{
}
void get_USBDevice_ifaces(void *s)
{
}
// USBPort
void get_USBPort_dev(void *s)
{
}
void get_USBPort_speedmask(void *s)
{
}
void get_USBPort_hubcount(void *s)
{
}
void get_USBPort_path(void *s)
{
}
void get_USBPort_ops(void *s)
{
}
void get_USBPort_opaque(void *s)
{
}
void get_USBPort_index(void *s)
{
}
void get_USBPort_next(void *s)
{
}
// USBDescriptor

void get_USBDescriptor_Device_bLength(void *s)
{
}
void get_USBDescriptor_Device_bcdUSB_lo(void *s)
{
}
void get_USBDescriptor_Device_bcdUSB_hi(void *s)
{
}
void get_USBDescriptor_Device_bDeviceClass(void *s)
{
}
void get_USBDescriptor_Device_bDeviceSubClass(void *s)
{
}
void get_USBDescriptor_Device_bDeviceProtocol(void *s)
{
}
void get_USBDescriptor_Device_bMaxPacketSize0(void *s)
{
}
void get_USBDescriptor_Device_idVendor_lo(void *s)
{
}
void get_USBDescriptor_Device_idVendor_hi(void *s)
{
}
void get_USBDescriptor_Device_idProduct_lo(void *s)
{
}
void get_USBDescriptor_Device_idProduct_hi(void *s)
{
}
void get_USBDescriptor_Device_bcdDevice_lo(void *s)
{
}
void get_USBDescriptor_Device_bcdDevice_hi(void *s)
{
}
void get_USBDescriptor_Device_iManufacturer(void *s)
{
}
void get_USBDescriptor_Device_iProduct(void *s)
{
}
void get_USBDescriptor_Device_iSerialNumber(void *s)
{
}
void get_USBDescriptor_Device_bNumConfigurations(void *s)
{
}

void get_USBDescriptor_Config_wTotalLength_lo(void *s)
{
}
void get_USBDescriptor_Config_wTotalLength_hi(void *s)
{
}
void get_USBDescriptor_Config_bNumInterfaces(void *s)
{
}
void get_USBDescriptor_Config_bConfigurationValue(void *s)
{
}
void get_USBDescriptor_Config_iConfiguration(void *s)
{
}
void get_USBDescriptor_Config_bmAttributes(void *s)
{
}
void get_USBDescriptor_Config_bMaxPower(void *s)
{
}

void get_USBDescriptor_Interface_bInterfaceNumber(void *s)
{
}
void get_USBDescriptor_Interface_bAlternateSetting(void *s)
{
}
void get_USBDescriptor_Interface_bNumEndpoints(void *s)
{
}
void get_USBDescriptor_Interface_bInterfaceClass(void *s)
{
}
void get_USBDescriptor_Interface_bInterfaceSubClass(void *s)
{
}
void get_USBDescriptor_Interface_bInterfaceProtocol(void *s)
{
}
void get_USBDescriptor_Interface_iInterface(void *s)
{
}

void get_USBDescriptor_Endpoint_bEndpointAddress(void *s)
{
}
void get_USBDescriptor_Endpoint_bmAttributes(void *s)
{
}
void get_USBDescriptor_Endpoint_wMaxPacketSize_lo(void *s)
{
}
void get_USBDescriptor_Endpoint_wMaxPacketSize_hi(void *s)
{
}
void get_USBDescriptor_Endpoint_bInterval(void *s)
{
}
void get_USBDescriptor_Endpoint_bRefresh(void *s)
{
}
void get_USBDescriptor_Endpoint_bSynchAddress(void *s)
{
}

void get_USBDescriptor_Device_qualifier_bcdUSB_lo(void *s)
{
}
void get_USBDescriptor_Device_qualifier_bcdUSB_hi(void *s)
{
}
void get_USBDescriptor_Device_qualifier_bDeviceClass(void *s)
{
}
void get_USBDescriptor_Device_qualifier_bDeviceSubClass(void *s)
{
}
void get_USBDescriptor_Device_qualifier_bDeviceProtocol(void *s)
{
}
void get_USBDescriptor_Device_qualifier_bMaxPacketSize0(void *s)
{
}
void get_USBDescriptor_Device_qualifier_bNumConfigurations(void *s)
{
}
void get_USBDescriptor_Device_qualifier_bReserved(void *s)
{
}

void get_USBDescriptor_Other_speed_config_(void *s)
{
}
void get_USBDescriptor_Other_speed_config_(void *s)
{
}
void get_USBDescriptor_Other_speed_config_(void *s)
{
}
void get_USBDescriptor_Other_speed_config_(void *s)
{
}
void get_USBDescriptor_Other_speed_config_(void *s)
{
}

void get_USBDescriptor_endpoint_companion_bMaxBurst(void *s)
{
}
void get_USBDescriptor_endpoint_companion_bmAttributes(void *s)
{
}
void get_USBDescriptor_endpoint_companion_wBytesPerInterval_lo(void *s)
{
}
void get_USBDescriptor_endpoint_companion_wTotalLength_hi(void *s)
{
}
void get_USBDescriptor_endpoint_companion_wBytesPerInterval_hi(void *s)
{
}

void get_USBDescriptor_Interface_assoc_bInterfaceNumber(void *s)
{
}
void get_USBDescriptor_Interface_assoc_bAlternateSetting(void *s)
{
}
void get_USBDescriptor_Interface_assoc_bNumEndpoints(void *s)
{
}
void get_USBDescriptor_Interface_assoc_bInterfaceClass(void *s)
{
}
void get_USBDescriptor_Interface_assoc_bInterfaceSubClass(void *s)
{
}
void get_USBDescriptor_Interface_assoc_bInterfaceProtocol(void *s)
{
}
void get_USBDescriptor_Interface_assoc_iInterface(void *s)
{
}

void get_USBDescriptor_Bos_wTotalLength_lo(void *s)
{
}
void get_USBDescriptor_Bos_wTotalLength_hi(void *s)
{
}
void get_USBDescriptor_Bos_bNumDeviceCaps(void *s)
{
}

void get_USBDescriptor_Device_capability_bmAttributes_1(void *s)
{
}
void get_USBDescriptor_Device_capability_bmAttributes_2(void *s)
{
}
void get_USBDescriptor_Device_capability_bmAttributes_3(void *s)
{
}
void get_USBDescriptor_Device_capability_bmAttributes_4(void *s)
{
}

void get_USBDescriptor_Cs_endpoint_bMaxBurst(void *s)
{
}
void get_USBDescriptor_Cs_endpoint_bmAttributes(void *s)
{
}
void get_USBDescriptor_Cs_endpoint_wBytesPerInterval_lo(void *s)
{
}
void get_USBDescriptor_Cs_endpoint_wBytesPerInterval_hi(void *s)
{
}

// USBDescID
void get_USBDescID_idVendor(void *s)
{
}
void get_USBDescID_idProduct(void *s)
{
}
void get_USBDescID_bcdDevice(void *s)
{
}
void get_USBDescID_iManufacturer(void *s)
{
}
void get_USBDescID_iProduct(void *s)
{
}
void get_USBDescID_iSerialNumber(void *s)
{
}
// USBDescDevice
void get_USBDescDevice_bcdUSB(void *s)
{
}
void get_USBDescDevice_bDeviceClass(void *s)
{
}
void get_USBDescDevice_bDeviceSubClass(void *s)
{
}
void get_USBDescDevice_bDeviceProtocol(void *s)
{
}
void get_USBDescDevice_bMaxPacketSize0(void *s)
{
}
void get_USBDescDevice_bNumConfigurations(void *s)
{
}
void get_USBDescDevice_confs(void *s)
{
}
// USBDescConfig
void get_USBDescConfig_bNumInterfaces(void *s)
{
}
void get_USBDescConfig_bConfigurationValue(void *s)
{
}
void get_USBDescConfig_iConfiguration(void *s)
{
}
void get_USBDescConfig_bmAttributes(void *s)
{
}
void get_USBDescConfig_bMaxPower(void *s)
{
}
void get_USBDescConfig_nif_groups(void *s)
{
}
void get_USBDescConfig_if_groups(void *s)
{
}
void get_USBDescConfig_nif(void *s)
{
}
void get_USBDescConfig_ifs(void *s)
{
}
// USBDescIfaceAssoc
void get_USBDescIfaceAssoc_bFirstInterface(void *s)
{
}
void get_USBDescIfaceAssoc_bInterfaceCount(void *s)
{
}
void get_USBDescIfaceAssoc_bFunctionClass(void *s)
{
}
void get_USBDescIfaceAssoc_bFunctionSubClass(void *s)
{
}
void get_USBDescIfaceAssoc_bFunctionProtocol(void *s)
{
}
void get_USBDescIfaceAssoc_iFunction(void *s)
{
}
void get_USBDescIfaceAssoc_nif(void *s)
{
}
void get_USBDescIfaceAssoc_ifs(void *s)
{
}
// USBDescIface
void get_USBDescIface_bInterfaceNumber(void *s)
{
}
void get_USBDescIface_bAlternateSetting(void *s)
{
}
void get_USBDescIface_bNumEndpoints(void *s)
{
}
void get_USBDescIface_bInterfaceClass(void *s)
{
}
void get_USBDescIface_bInterfaceSubClass(void *s)
{
}
void get_USBDescIface_bInterfaceProtocol(void *s)
{
}
void get_USBDescIface_iInterface(void *s)
{
}
void get_USBDescIface_ndesc(void *s)
{
}
void get_USBDescIface_descs(void *s)
{
}
void get_USBDescIface_eps(void *s)
{
}
// USBDescEndpoint
void get_USBDescEndpoint_bEndpointAddress(void *s)
{
}
void get_USBDescEndpoint_bmAttributes(void *s)
{
}
void get_USBDescEndpoint_wMaxPacketSize(void *s)
{
}
void get_USBDescEndpoint_bInterval(void *s)
{
}
void get_USBDescEndpoint_bRefresh(void *s)
{
}
void get_USBDescEndpoint_bSynchAddress(void *s)
{
}
void get_USBDescEndpoint_is_audio(void *s)
{
}
void get_USBDescEndpoint_extra(void *s)
{
}
void get_USBDescEndpoint_bMaxBurst(void *s)
{
}
void get_USBDescEndpoint_bmAttributes_super(void *s)
{
}
void get_USBDescEndpoint_wBytesPerInterval(void *s)
{
}
// USBDescOther
void get_USBDescOther_length(void *s)
{
}
void get_USBDescOther_data(void *s)
{
}
// USBDescMSOS
void get_USBDescMSOS_CompatibleID(void *s)
{
}
void get_USBDescMSOS_Label(void *s)
{
}
void get_USBDescMSOS_SelectiveSuspendEnabled(void *s)
{
}
// USBDesc
void get_USBDesc_id(void *s)
{
}
void get_USBDesc_full(void *s)
{
}
void get_USBDesc_high(void *s)
{
}
void get_USBDesc_super(void *s)
{
}
void get_USBDesc_str(void *s)
{
}
void get_USBDesc_msos(void *s)
{
}
