
#include "qemu/osdep.h"
#include "qapi/error.h"
#include "qemu/main-loop.h"
#include "qemu/module.h"
#include "hw/usb.h"
typedef struct USBBusOps USBBusOps;
typedef struct USBPort USBPort;
typedef struct USBDevice USBDevice;
typedef struct USBPacket USBPacket_;
typedef struct USBCombinedPacket USBCombinedPacket;
typedef struct USBEndpoint USBEndpoint;

typedef struct USBDesc USBDesc;
typedef struct USBDescID USBDescID;
typedef struct USBDescDevice USBDescDevice;
typedef struct USBDescConfig USBDescConfig;
typedef struct USBDescIfaceAssoc USBDescIfaceAssoc;
typedef struct USBDescIface USBDescIface;
typedef struct USBDescEndpoint USBDescEndpoint;
typedef struct USBDescOther USBDescOther;
typedef struct USBDescString USBDescString;
typedef struct USBDescMSOS USBDescMSOS;
// USBDevice
void glue_cancel_packet(USBDevice *dev, USBPacket *p);
void glue_handle_attach(USBDevice *dev);
void glue_handle_reset(USBDevice *dev);
void glue_handle_control(USBDevice *dev, USBPacket *p, int request, int value, int index, int length, uint8_t *data);
void glue_handle_data(USBDevice *dev, USBPacket *p);
void glue_set_interface(USBDevice *dev, int interface, int alt_old, int alt_new);
void glue_flush_ep_queue(USBDevice *dev, USBEndpoint *ep);
void glue_ep_stopped(USBDevice *dev, USBEndpoint *ep);
void glue_alloc_streams(USBDevice *dev, USBEndpoint **eps, int nr_eps, int streams);
void glue_free_streams(USBDevice *dev, USBEndpoint **eps, int nr_eps);

void glue_glue_dev(USBPort *port);
void glue_glue_detach(USBPort *port);
void glue_glue_child_detach(USBPort *port, USBDevice *child);
void glue_glue_wakeup(USBPort *port);
void glue_glue_complete(USBPort *port, USBPacket *p);
